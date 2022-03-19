#!/usr/bin/node
const request = require('request');
const ApiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieID = process.argv[2];

request(ApiUrl + movieID, (error, response, body) => {
  if (error) throw error;
  const characters = JSON.parse(body).characters;
  displayNames(characters);
});

const displayNames = (names, i = 0) => {
  if (i === names.length) return;
  request(names[i], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    displayNames(names, i + 1);
  });
};
