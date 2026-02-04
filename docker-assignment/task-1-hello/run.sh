#!/usr/bin/env bash
set -e

# variables you may update to target the correct file
IMAGE_NAME="task1-demo"
CONTAINER_NAME="task1-container"

# this will rebuild the image within the docker engine
echo "Building image: $IMAGE_NAME"
docker build --quiet -t "$IMAGE_NAME" .

# this will run the container and automatically remove it upon completion
echo "Running container with bind mount..."
docker run --rm --name "$CONTAINER_NAME" "$IMAGE_NAME"