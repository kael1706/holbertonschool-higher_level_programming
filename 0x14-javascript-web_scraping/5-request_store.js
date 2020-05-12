#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
require('request').get(process.argv[2], (e, r, d) => {
  if (e) {
    console.log(e);
  } else {
    require('fs').writeFile(process.argv[3], d, 'utf-8', (e) => {
      if (e) {
        console.log(e);
      }
    });
  }
});
