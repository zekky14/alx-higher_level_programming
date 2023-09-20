#!/bin/bash

curl -s -o - "$1" | tail -n+2 | wc -c
