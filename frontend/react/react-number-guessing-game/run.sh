# Builds the image (only needed once)
#docker build --quiet -t my-vite-image .

# Make a container (change --name depending on project (or don't, it's cool))
docker run \
  --rm \
  -p 5173:5173 \
  -v $(pwd):/app \
  -v /app/node_modules \
  --name react-container \
  my-vite-image