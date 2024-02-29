#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, displays the body of the response
curl -sI 54.85.90.192:80 | grep "Content-Length" | awk '{print $2}'
