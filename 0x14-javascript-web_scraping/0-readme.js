#!/usr/bin/node
// reads and prints the content of a file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (e, res) => {
  if (e) {
    console.log(e);
  } else {
    console.log(res.toString().trim());
  }
});
