#!/usr/bin/env bash
set -e

# variables you may update to target the correct file
IMAGE_NAME="js-demo"
CONTAINER_NAME="js-container"
FOLDER="algo-factorial"
FILE="factorialSpec.js"

set_folder_and_file () {
    case $1 in
        f) FOLDER="algo-factorial"
                FILE="factorialSpec.js";;
        r) FOLDER="algo-roman-numerals"
            FILE="romanNumeralsSpec.js";;
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