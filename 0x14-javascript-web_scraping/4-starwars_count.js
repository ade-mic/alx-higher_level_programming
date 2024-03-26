#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
//  prints the title of a Star Wars movie where the episode number matches a given integer.
request(api, function (error, response, body) {
  if (error) throw error;
  else if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const movieWithWedge = data.results.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(movieWithWedge.length);
  }
});
