#!/usr/bin/node
// increments and calls a function.
exports.addMeMaybe = (n, Function) => {
	  Function(n + 1);
};
