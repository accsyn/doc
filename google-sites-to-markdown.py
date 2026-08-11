#!/usr/bin/env python3

import argparse
import asyncio
import hashlib
import mimetypes
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import async_playwright


SKIP_SCHEMES = (
    "mailto:",
    "tel:",
    "javascript:",
)

IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
}


def normalize_url(url: str) -> str:
    url, _fragment = urldefrag(url)
    return url.rstrip("/")


def is_same_site(url: str, root_url: str) -> bool:
    a = urlparse(url)
    b = urlparse(root_url)

    if a.netloc != b.netloc:
        return False

    # Important for sites.google.com where multiple sites share the same host.
    root_path = b.path.rstrip("/")
    return a.path.startswith(root_path)


def safe_slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-") or "index"


def page_output_path(url: str, root_url: str, output_dir: Path) -> Path:
    root = urlparse(root_url)
    parsed = urlparse(url)

    root_parts = [p for p in root.path.split("/") if p]
    page_parts = [p for p in parsed.path.split("/") if p]

    relative_parts = page_parts[len(root_parts):]

    if not relative_parts:
        return output_dir / "index.md"

    relative_parts = [safe_slug(p) for p in relative_parts]

    return output_dir.joinpath(*relative_parts).with_suffix(".md")


def extract_image_url(img, base_url: str) -> str | None:
    candidates = [
        img.get("src"),
        img.get("data-src"),
        img.get("data-original"),
    ]

    srcset = img.get("srcset")
    if srcset:
        # Take the highest-resolution/last candidate.
        parts = [x.strip().split(" ")[0] for x in srcset.split(",")]
        if parts:
            candidates.insert(0, parts[-1])

    for candidate in candidates:
        if candidate and not candidate.startswith("data:"):
            return urljoin(base_url, candidate)

    return None


def extension_from_response(url: str, content_type: str | None) -> str:
    parsed = urlparse(url)
    ext = Path(parsed.path).suffix.lower()

    if ext in IMAGE_EXTENSIONS:
        return ext

    if content_type:
        content_type = content_type.split(";")[0]
        guessed = mimetypes.guess_extension(content_type)
        if guessed:
            return guessed

    return ".img"


def download_image(
    image_url: str,
    assets_dir: Path,
    session: requests.Session,
    page_slug: str,
) -> Path | None:

    try:
        response = session.get(image_url, timeout=30)
        response.raise_for_status()
    except Exception as exc:
        print(f"    ! Failed image: {image_url}: {exc}")
        return None

    content_type = response.headers.get("Content-Type")
    ext = extension_from_response(image_url, content_type)

    digest = hashlib.sha1(image_url.encode("utf-8")).hexdigest()[:12]

    parsed = urlparse(image_url)
    original_name = Path(parsed.path).stem
    original_name = safe_slug(original_name)

    # Google-hosted images use very long opaque tokens as path names,
    # which exceed filesystem filename limits. Only keep the original
    # name when it is short and meaningful; the digest already makes
    # the filename unique.
    if (
        not original_name
        or original_name == "index"
        or len(original_name) > 40
    ):
        original_name = ""

    parts = [p for p in [page_slug, original_name] if p]
    filename = f"{'_'.join(parts)}-{digest}{ext}"

    assets_dir.mkdir(parents=True, exist_ok=True)

    path = assets_dir / filename
    path.write_bytes(response.content)

    return path


def find_main_content(soup: BeautifulSoup):
    """
    Google Sites markup changes occasionally, so use a layered strategy.
    """

    candidates = [
        soup.find("main"),
        soup.find(attrs={"role": "main"}),
        soup.find("article"),
    ]

    candidate = next((c for c in candidates if c), None)

    # Google Sites frequently stores the actual page content in <section>
    # elements that live OUTSIDE the role="main" element (which may only
    # contain the page banner). Prefer the sections when they hold more text
    # than the candidate container. Sections inside the site footer are
    # excluded, as they only contain boilerplate repeated on every page.
    sections = [
        s for s in soup.select("section")
        if not s.find_parent("footer")
    ]

    if sections:
        sections_text = sum(
            len(s.get_text(strip=True)) for s in sections
        )
        candidate_text = (
            len(candidate.get_text(strip=True)) if candidate else 0
        )

        if sections_text > candidate_text:
            wrapper = soup.new_tag("div")
            for section in sections:
                wrapper.append(section.extract())
            return wrapper

    if candidate:
        return candidate

    return soup.body or soup


def clean_html(content):
    # Remove obvious UI / navigation / script noise.
    selectors = [
        "script",
        "style",
        "noscript",
        "nav",
        "header",
        "footer",
        "button",
        "[role='navigation']",
        "[aria-hidden='true']",
    ]

    for selector in selectors:
        for element in content.select(selector):
            element.decompose()

    # Remove empty elements that often come from Google Sites layout.
    for tag in content.find_all(["div", "span", "p"]):
        if not tag.get_text(strip=True) and not tag.find("img"):
            tag.decompose()


def title_from_soup(soup: BeautifulSoup, url: str) -> str:
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(" ", strip=True)
        if title:
            return title

    if soup.title:
        title = soup.title.get_text(" ", strip=True)
        title = re.sub(r"\s*-\s*Google Sites\s*$", "", title)
        if title:
            return title

    parsed = urlparse(url)
    return Path(parsed.path).name or "Home"


def rewrite_links(
    content,
    current_url: str,
    root_url: str,
    current_output: Path,
    output_dir: Path,
):
    for anchor in content.find_all("a", href=True):
        href = anchor["href"]

        if href.startswith(SKIP_SCHEMES):
            continue

        absolute = normalize_url(urljoin(current_url, href))

        if not is_same_site(absolute, root_url):
            anchor["href"] = absolute
            continue

        target_output = page_output_path(
            absolute,
            root_url,
            output_dir,
        )

        try:
            relative = target_output.relative_to(current_output.parent)
        except ValueError:
            import os
            relative = Path(
                os.path.relpath(target_output, current_output.parent)
            )

        anchor["href"] = relative.as_posix()


def convert_page(
    html: str,
    url: str,
    root_url: str,
    output_dir: Path,
    session: requests.Session,
):
    soup = BeautifulSoup(html, "html.parser")

    title = title_from_soup(soup, url)

    content = find_main_content(soup)
    clean_html(content)

    output_path = page_output_path(
        url,
        root_url,
        output_dir,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    assets_dir = output_dir / "assets"

    # Page URI relative to the site root, underscore delimited,
    # used to prefix downloaded image filenames.
    page_slug = "_".join(
        output_path.relative_to(output_dir).with_suffix("").parts
    )

    # Download images and replace their URLs.
    for image in content.find_all("img"):
        image_url = extract_image_url(image, url)

        if not image_url:
            continue

        local_path = download_image(
            image_url,
            assets_dir,
            session,
            page_slug,
        )

        if not local_path:
            continue

        import os

        relative = Path(
            os.path.relpath(local_path, output_path.parent)
        )

        image["src"] = relative.as_posix()

        # Remove Google-specific lazy loading.
        for attr in [
            "srcset",
            "data-src",
            "data-original",
        ]:
            image.attrs.pop(attr, None)

    rewrite_links(
        content,
        url,
        root_url,
        output_path,
        output_dir,
    )

    markdown = md(
        str(content),
        heading_style="ATX",
        bullets="-",
        strip=["span"],
    )

    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = markdown.strip()

    # Only add H1 if the page content does not already begin with one.
    if not re.match(r"^\s*# ", markdown):
        markdown = f"# {title}\n\n{markdown}"

    output_path.write_text(
        markdown + "\n",
        encoding="utf-8",
    )

    print(f"  -> {output_path}")

    return output_path


async def get_internal_links(page, current_url: str, root_url: str):
    links = await page.locator("a[href]").evaluate_all(
        """
        elements => elements.map(a => a.href)
        """
    )

    result = set()

    for link in links:
        if not link:
            continue

        link = normalize_url(link)

        if link.startswith(SKIP_SCHEMES):
            continue

        if is_same_site(link, root_url):
            result.add(link)

    return result


async def crawl(root_url: str, output_dir: Path):
    root_url = normalize_url(root_url)

    todo = [root_url]
    visited = set()

    session = requests.Session()

    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 GoogleSitesMarkdownMigration/1.0"
        )
    })

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
        )

        context = await browser.new_context(
            viewport={
                "width": 1440,
                "height": 1200,
            }
        )

        page = await context.new_page()

        while todo:
            url = todo.pop(0)

            if url in visited:
                continue

            visited.add(url)

            print()
            print(f"[{len(visited)}] {url}")

            try:
                await page.goto(
                    url,
                    wait_until="networkidle",
                    timeout=60_000,
                )
            except Exception as exc:
                print(f"  ! Navigation error: {exc}")
                continue

            # Give late-loaded Google Sites content a little time.
            await page.wait_for_timeout(1000)

            html = await page.content()

            convert_page(
                html,
                url,
                root_url,
                output_dir,
                session,
            )

            links = await get_internal_links(
                page,
                url,
                root_url,
            )

            for link in sorted(links):
                if link not in visited and link not in todo:
                    todo.append(link)

        await browser.close()

    print()
    print(f"Done. Crawled {len(visited)} pages.")
    print(f"Output: {output_dir.resolve()}")


def main():
    parser = argparse.ArgumentParser(
        description="Export a public Google Site to Markdown."
    )

    parser.add_argument(
        "url",
        help="Root URL of the published Google Site",
    )

    parser.add_argument(
        "output",
        nargs="?",
        default="./google-sites-export",
        help="Output directory",
    )

    args = parser.parse_args()

    asyncio.run(
        crawl(
            args.url,
            Path(args.output),
        )
    )


if __name__ == "__main__":
    main()
