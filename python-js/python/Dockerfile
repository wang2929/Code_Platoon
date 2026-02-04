FROM python:3.11-slim
ARG FOLDER
ARG FILE
ENV FOLDER=${FOLDER:-algo-fibonacci-py}
ENV FILE=${FILE:-fibonacci_spec.py}

WORKDIR /app
COPY ./$FOLDER /app
CMD python3 /app/$FILE
# creates a simple python environment and runs FILE from FOLDER