#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi.dev/api/films/';

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Make a request to the Star Wars API to get the film data
request(`${apiUrl}${movieId}`, { json: true }, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  const film = body;

  // Create a function that will fetch a character name
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, { json: true }, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body.name);
        }
      });
    });
  };

  // Fetch each character's name in the order they appear in the film
  const fetchAllCharacters = async () => {
    for (const charUrl of film.characters) {
      try {
        const name = await fetchCharacterName(charUrl);
        console.log(name);
      } catch (error) {
        console.error('Error fetching character name:', error);
      }
    }
  };

  fetchAllCharacters();
});
