#!/bin/bash

curl -s -o - "$1" | tail -n+2 | cut -f2- | head -n1 | bc -l
