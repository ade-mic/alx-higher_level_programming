#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

// input from cmd line
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', function (err) {
      if (err) throw err;
    });
  }
});
