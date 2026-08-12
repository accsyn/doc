#!/usr/bin/env bash
#
# Build (and optionally push) the accsyn-doc Docker image.
#
# Usage:
#   ./docker-build.sh                  Build accsyn-doc:latest locally
#   ./docker-build.sh myuser           Build and push myuser/accsyn-doc:latest
#   ./docker-build.sh myuser 2026.1    Build and push myuser/accsyn-doc:2026.1

set -euo pipefail

cd "$(dirname "$0")"

DOCKERHUB_USER="${1:-}"
TAG="${2:-latest}"
IMAGE="accsyn-doc"

docker build -t "${IMAGE}:${TAG}" .

if [ -n "${DOCKERHUB_USER}" ]; then
    docker tag "${IMAGE}:${TAG}" "${DOCKERHUB_USER}/${IMAGE}:${TAG}"
    docker push "${DOCKERHUB_USER}/${IMAGE}:${TAG}"
    echo "Pushed ${DOCKERHUB_USER}/${IMAGE}:${TAG}"
else
    echo "Built ${IMAGE}:${TAG} (pass your Docker Hub username to push)"
fi
