#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
request(process.argv[2], function (e, r, d) {
  if (e) {
    console.log(e);
  } else {
    const value = {};
    const tasks = JSON.parse(d);
    for (let i = 0; i < tasks.length; ++i) {
      if (tasks[i].completed) {
        if (!(tasks[i].userId in value)) {
          value[tasks[i].userId] = 0;
        }
        value[tasks[i].userId] += 1;
      }
    }
    console.log(value);
  }
});
