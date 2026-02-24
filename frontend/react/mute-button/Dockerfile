FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install

EXPOSE 5174

CMD ["npm", "run", "dev"]