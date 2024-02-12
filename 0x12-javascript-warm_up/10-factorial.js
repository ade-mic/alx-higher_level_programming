#!/usr/bin/node
const arg = parseInt(process.argv[2]);
let value;
if (isNaN(arg)) {
  value = 1;
} else {
  value = arg;
}

// create factorial()
function factorial (a) {
  if (a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

// use factorial()
console.log(factorial(value));
