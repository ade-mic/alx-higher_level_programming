#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  const width = size;
  let height = size;
  while (height > 0) {
    console.log('X'.repeat(width));
    height--;
  }
}
