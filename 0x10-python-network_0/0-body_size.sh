#!/bin/bash
# send URL request, extracting the content length from the response, counting the bytes in the response body
curl -s -o - "$1" | tail -n+2 | wc -c
