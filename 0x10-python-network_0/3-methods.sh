#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -siX allow '$1'| grep -i '^allow:'
