# accsyn Documentation

This repository stores the new 2026 documentation using MkDocs, deprecating the previous Google Sites implementation.

## Converting from Google Sites

```
pyenv virtualenv accsyn-doc
pyenv activate accsyn-doc
pip install playwright beautifulsoup4 markdownify requests
playwright install chromium --with-deps
python google-sites-to-markdown.py https://support.accsyn.com legacy-google-sites/
```
