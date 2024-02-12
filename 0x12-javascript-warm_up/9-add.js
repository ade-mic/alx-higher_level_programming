#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

// create ad function
function add (a, b) {
  // check if argument passed is int
  if (isNaN(a) || a === undefined || isNaN(b) || b === undefined) {
    return NaN;
  }
  return (a + b);
}

// call add function
console.log(add(firstArg, secondArg));
