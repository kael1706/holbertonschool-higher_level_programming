#!/usr/bin/node
// Display the status code of a GET request.
const request = require('request');
request(process.argv[2], function (e, r) {
  if (e) {
    console.log(e);
  } else {
    console.log('code: ' + r.statusCode);
  }
});
