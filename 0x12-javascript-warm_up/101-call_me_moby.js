#!/usr/bin/node
// function that can call other repeatedly
exports.callMeMoby = (a, Function) => {
  for (let i = 0; i < a; i++) {
    Function();
  }
};
