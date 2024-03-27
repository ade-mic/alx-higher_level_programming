#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(api, function (error, response, body) {
  if (error) throw error;
  else if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);

    const res = data.results.filter(movie =>
      movie.characters.includes(characterUrl));
    const count = res.length;
    console.log(count);
  }
});
