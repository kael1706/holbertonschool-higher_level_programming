#!/usr/bin/node
// know if first arg is a number
const n = parseInt(process.argv[2]);
if (n) {
  console.log('My number: ' + n);
} else {
  console.log('Not a number');
}
