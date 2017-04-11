#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -ILs "$1" | grep Allow | cut -d':' -f2 | tr -d ' '
