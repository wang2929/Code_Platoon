FROM node:latest
WORKDIR /app
COPY . .
RUN npm install --legacy-peer-deps && \
    npm install tailwindcss @tailwindcss/vite
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