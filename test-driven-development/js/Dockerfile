FROM node:18-alpine
ARG FOLDER
ENV FOLDER=${FOLDER:-algo-fibonacci}

WORKDIR /app
COPY ./$FOLDER /app
COPY package*.json ./
RUN npm install
RUN npm install --save-dev jest
CMD ["npm", "test"]
# creates a simple python environment and runs FILE from FOLDER