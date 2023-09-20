#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -o - -I "$1" | grep -q 200 |  echo "$(curl -s -o - -I "$1")"
