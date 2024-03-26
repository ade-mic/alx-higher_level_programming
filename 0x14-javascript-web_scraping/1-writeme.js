#!/usr/bin/node
const fs = require('fs');

// write a file
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
