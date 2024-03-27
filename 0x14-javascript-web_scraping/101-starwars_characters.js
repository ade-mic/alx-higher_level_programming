#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi.dev/api/films/';

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Make a request to the Star Wars API to get the film data
request(`${apiUrl}${movieId}`, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  const film = JSON.parse(body);

  // Create a function that will fetch a character name
  const fetchCharacterName = (url, callback) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('An error occurred:', error);
        return;
      }

      const character = JSON.parse(body);
      callback(character.name);
    });
  };

  // Fetch each character's name in the order they appear in the film
  for (const char of film.characters) {
    fetchCharacterName(char, (name) => {
      console.log(name);
    });
  }
//   film.characters.forEach((characterUrl) => {
//     fetchCharacterName(characterUrl, (name) => {
//       console.log(name);
//     });
//   });
});
