#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const film = JSON.parse(body);
  const charactersUrls = film.characters;

  const fetchCharacter = (url) => {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
        process.exit(1);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  };

  charactersUrls.forEach(fetchCharacter);
});

