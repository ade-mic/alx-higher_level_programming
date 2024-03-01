#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
#!/bin/bash
curl -sI "$1" | grep 200 | curl -s "$1"
