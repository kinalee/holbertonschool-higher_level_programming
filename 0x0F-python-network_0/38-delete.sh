#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -L "$1" -X DELETE
