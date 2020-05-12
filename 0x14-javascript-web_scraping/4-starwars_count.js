#!/usr/bin/node
// prints the number of movies
// where the character “Wedge Antilles” is present.
const request = require('request');
request(process.argv[2], (e, r, d) => {
  if (e) {
    console.log(e);
  } else {
    let c = 0;
    const films = JSON.parse(d).results;
    for (let i = 0; i < films.length; ++i) {
      for (let j = 0; j < films[i].characters.length; ++j) {
        if (films[i].characters[j].includes('/18/')) {
          c++;
          break;
        }
      }
    }
    console.log(c);
  }
});
