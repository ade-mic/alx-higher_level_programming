#!/usr/bin/node
const request = require('request');
// display the status code of a GET request.
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
