#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Check if URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Use curl to get the body size in bytes
size=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')

# Check if size is empty (Content-Length not present)
if [ -z "$size" ]; then
    echo "Content-Length not found in the headers."
else
    # Display the size
    echo "$size"
fi

