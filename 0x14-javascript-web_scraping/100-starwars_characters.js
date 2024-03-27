#!/usr/bin/node
const request = require('request');

let movieId = process.argv[2];  // Replace with your Movie ID
let api = `https://swapi.dev/api/films/${movieId}/`;

request(api, function (error, response, body) {
  if (error) throw error;
  else if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    let characters = film.characters;

    characters.forEach(function(character) {
      request(character, function (error, response, body) {
        if (error) throw error;
        else if (!error && response.statusCode === 200) {
          const characterInfo = JSON.parse(body);
          console.log(characterInfo.name);
        }
      });
    });
  }
});
