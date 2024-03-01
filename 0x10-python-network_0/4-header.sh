#!/bin/bash
# script sends a GET request using curl, includes the X-School-User-Id header with the value 98, and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
