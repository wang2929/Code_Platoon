# Builds the image (only needed once)
docker build --quiet -t mute-button-image .

# Make a container (change --name depending on project (or don't, it's cool))
docker run \
  --rm \
  -p 5174:5174 \
  -v $(pwd):/app \
  -v /app/node_modules \
  --name mute-button-container \
  mute-button-image