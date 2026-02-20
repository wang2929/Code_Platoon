# Builds the image (only needed once)
docker build --quiet -t vowels-image .

# Make a container (change --name depending on project (or don't, it's cool))
docker run \
  --rm \
  -p 5173:5173 \
  -v $(pwd):/app \
  -v /app/node_modules \
  --name vowels-container \
  vowels-image