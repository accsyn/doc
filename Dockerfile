# Build the MkDocs site
FROM python:3.12-slim AS build

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mkdocs.yml .
COPY docs/ docs/

RUN mkdocs build --strict

# Serve the static site with nginx
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /build/site/ /usr/share/nginx/html/

EXPOSE 80
