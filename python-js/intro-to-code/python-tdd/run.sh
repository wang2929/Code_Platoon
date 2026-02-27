#!/usr/bin/env bash
set -e

# variables you may update to target the correct file
IMAGE_NAME="py-demo"
CONTAINER_NAME="py-container"
FOLDER="algo-roman-numeral-py"
FILE="test_roman_numerals.py"

set_folder_and_file () {
    case $1 in
        r) FOLDER="algo-roman-numeral-py"
                FILE="test_roman_numerals.py";;
        s) FOLDER="algo-linear-search-py"
            FILE="test_linear_search.py";;
        c) FOLDER="intro_to_pytest"
            FILE="test_calculator.py" ;;
        *) echo "Not a valid file/folder alias."
            exit -1 ;;
    esac
}

# Check for flags
while getopts "f:" flag; do
    case "${flag}" in
        f) set_folder_and_file ${OPTARG} ;;
    esac
done

# this will rebuild the image within the docker engine
echo "Building image: $IMAGE_NAME" 
docker build --quiet -t "$IMAGE_NAME" --build-arg FOLDER=$FOLDER --build-arg FILE=$FILE .

# this will run the container and automatically remove it upon completion
echo "Running container with bind mount..."
docker run --rm --name "$CONTAINER_NAME" "$IMAGE_NAME"