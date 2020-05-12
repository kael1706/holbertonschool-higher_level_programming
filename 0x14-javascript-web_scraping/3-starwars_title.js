#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (e, r, d) => {
  if (e) {
    console.log(e);
  } else {
    console.log(JSON.parse(d).title);
  }
});
