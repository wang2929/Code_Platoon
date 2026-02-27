#!/usr/bin/env bash
set -e

# variables you may update to target the correct file
IMAGE_NAME="py-demo"
CONTAINER_NAME="py-container"
FOLDER="algo-factorial-py"
FILE="factorial_spec.py"

set_folder_and_file () {
    case $1 in
        fac) FOLDER="algo-factorial-py"
                FILE="factorial_spec.py";;
        b) FOLDER="algo-99-bottles-py"
            FILE="bottles.py";;
        fib) FOLDER="algo-fibonacci-py"
            FILE="fibonacci_spec.py";;
        *) echo "Not a valid file/folder alias."
            exit -1 ;;
    esac
}

# Check for flags
while getopts "i:c:f:" flag; do
    case "${flag}" in
        i) IMAGE_NAME=${OPTARG} ;;
        c) CONTAINER_NAME=${OPTARG} ;;
        f) set_folder_and_file ${OPTARG} ;;
    esac
done

# this will rebuild the image within the docker engine
echo "Building image: $IMAGE_NAME" 
docker build --quiet -t "$IMAGE_NAME" --build-arg FOLDER=$FOLDER --build-arg FILE=$FILE .

# this will run the container and automatically remove it upon completion
echo "Running container with bind mount..."
docker run --rm --name "$CONTAINER_NAME" "$IMAGE_NAME"