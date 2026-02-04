FROM node:18-alpine
ENV FOLDER=${FOLDER:-algo-fibonacci-py}
ENV FILE=${FILE:-fibonacci_spec.py}

WORKDIR /app
COPY ./$FOLDER .
CMD node /app/$FILE
# creates simple docker for node and runs FILE from FOLDER