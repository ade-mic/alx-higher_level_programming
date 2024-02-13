#!/usr/bin/node
let numbArgs = 0;
exports.logMe = function (item) {
  console.log(numbArgs + ': ' + item);
  numbArgs++;
};
