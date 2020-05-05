#!/usr/bin/node
// replace the value 12 with 89
// const is mutable
const obj = {
  type: 'object',
  value: 12
};
console.log(obj);
obj.value = 89;
console.log(obj);
