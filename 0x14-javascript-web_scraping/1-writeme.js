#!/usr/bin/node
// write a string to a file. (overwrite)
const fs = require('fs');
const words = process.argv[3];

fs.writeFile(process.argv[2], words, (e) => {
  if (e) {
    console.log(e);
  }
});
