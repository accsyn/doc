# accsyn Documentation

This repository stores the new 2026 documentation using MkDocs, deprecating the previous Google Sites implementation.

- `docs/` - The documentation source (Markdown), served at https://support.accsyn.com.
- `mkdocs.yml` - MkDocs configuration and site navigation.
- `legacy-google-sites/` - Untouched archive of the old Google Sites export.

## Working on the documentation

```
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000 to preview with live reload. `mkdocs build --strict` builds the static site into `site/` and fails on broken links.

URLs mirror the previous Google Site: `docs/delivery/index.md` is served at `/delivery/`, `docs/delivery/create.md` at `/delivery/create/`, and so on.

## Building and deploying the Docker image

The `accsyn-doc` image builds the site and serves it with nginx on port 80, intended to run behind the existing reverse proxy.

```
./docker-build.sh                  # Build accsyn-doc:latest locally
./docker-build.sh <dockerhub-user> # Build and push <dockerhub-user>/accsyn-doc:latest
./docker-build.sh <dockerhub-user> 2026.1 # Build and push a versioned tag
```

Run it locally for a smoke test:

```
docker run --rm -p 8080:80 accsyn-doc:latest
```

## Converting from Google Sites

```
pyenv virtualenv accsyn-doc
pyenv activate accsyn-doc
pip install playwright beautifulsoup4 markdownify requests
playwright install chromium --with-deps
python google-sites-to-markdown.py https://support.accsyn.com legacy-google-sites/
```
