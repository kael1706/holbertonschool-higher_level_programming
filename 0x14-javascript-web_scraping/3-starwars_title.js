#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
request('https://swapi.co/api/films/' + process.argv[2], (e, r, d) => {
  if (e) {
    console.log(e);
  } else {
    console.log(JSON.parse(d).title);
  }
});
