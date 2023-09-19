#!/usr/bin/bash
read url
curl -s -o - "$url" | tail -n+2 | cut -f2- | grep 200 | grep -o '<body>.*</body>
