#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 2) {
  console.log('No arguement');
} else if (argv.length === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
