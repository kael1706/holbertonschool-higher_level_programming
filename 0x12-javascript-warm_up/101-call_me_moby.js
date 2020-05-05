#!/usr/bin/node
// function that can call other repeatedly
exports.callMeMoby = (n, f) => {
  for (let i = 0; i < n; i++) {
    f();
  }
};
