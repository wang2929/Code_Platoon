FROM python:3.11-slim
ARG FOLDER
ARG FILE
ENV FOLDER=${FOLDER:-algo-roman-numeral-py}
ENV FILE=${FILE:-test_roman_numerals.py}

WORKDIR /app
COPY ./$FOLDER /app
RUN pip install --no-cache-dir pytest
CMD pytest /app/$FILE
# creates a simple python environment and runs FILE from FOLDER