#!/bin/bash

# Define the URL
url="$1"

# Send a request to the URL and store the response body in a variable
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size of the response body in bytes
echo "The size of the response body is $response bytes."
