#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
//  prints the title of a Star Wars movie where the episode number matches a given integer.
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
  if (error) throw error;
  else if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
