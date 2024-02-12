#!/usr/bin/node
const message = 'C is fun';
let args = parseInt(process.argv[2]);
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  while (args > 0) {
    console.log(message);
    args--;
  }
}
