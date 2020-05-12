#!/usr/bin/node
// Returns the reversed version of a list
exports.esrever = function (list) {
  const r = [];
  for (let i = list.length - 1; i >= 0; --i) {
    r.push(list[i]);
  }
  return r;
};
