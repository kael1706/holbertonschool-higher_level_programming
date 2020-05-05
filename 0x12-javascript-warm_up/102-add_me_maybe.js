#!/usr/bin/node
// increments and calls a function.
exports.addMeMaybe = (n, f) => {
  f(n + 1);
};
