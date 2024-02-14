#!/usr/bin/node
const fs = require('fs');
if (process.argv.length !== 5) {
  console.error('Usage: node concat.js <file1> <file2> <output>');
  process.exit(1);
}
const [fileA, fileB, fileC] = process.argv.slice(2);
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;
    fs.writeFile(fileC, dataA + dataB, (err) => {
      if (err) throw err;
    });
  });
});
