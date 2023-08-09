#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const promises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    Promise.all(promises)
      .then(names => {
        names.sort();
        for (const name of names) {
          console.log(name);
        }
      })
      .catch(error => {
        console.error(error);
      });
  }
});

