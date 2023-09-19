#!/usr/bin/python3
curl -s -o - "$1" | tail -n+2 | cut -f2- | bc -l
