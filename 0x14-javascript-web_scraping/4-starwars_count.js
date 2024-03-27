#!/usr/bin/node
const request = require('request');
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(characterUrl, function (error, response, body) {
  if (error) throw error;
  else if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const films = data.films;
    console.log(films.length);
  }
});
