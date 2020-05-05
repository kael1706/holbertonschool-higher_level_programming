#!/usr/bin/node
/* show 3 msg but with loop
 msgs.forEach(item => { console.log(item); });
*/
const msgs = [
  'C is fun',
  'Python is cool',
  'Javascript is amazing'
];
for (let i = 0; i < msgs.length; i++) {
  console.log(msgs[i]);
}
