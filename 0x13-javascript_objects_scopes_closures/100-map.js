#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map(item => list.indexOf(item) * item);
console.log(list);
console.log(newList);
