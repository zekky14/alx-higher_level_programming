#!/usr/bin/bash
read url
curl -s -o - "$url" | tail -n+2 | cut -f2- | grep 200
if [ "$?" -eq 0 ]; then
echo "$(echo "$url" | grep -o '<body>.*</body>')"
else
echo "ERROR: Response status is not 200"
fi
