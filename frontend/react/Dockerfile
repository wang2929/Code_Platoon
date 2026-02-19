# template for building image, though for EVERY project
# you have to rebuild image to re-install dependencies

FROM node:18
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 5173
CMD ["npm", "run", "dev"]

# Run command: 
# docker run \
#   --rm \
#   -p 5173:5173 \
#   -v $(pwd):/app \
#   -v /app/node_modules \
#   --name react-container \
#   my-vite-image