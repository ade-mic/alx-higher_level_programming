#!/usr/bin/node
const number = Number(process.argv[2]);
if (isNaN(number) || number === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(number));
}
