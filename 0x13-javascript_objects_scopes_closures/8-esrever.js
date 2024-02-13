#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  list.forEach(item => {
    newList.unshift(item);
  });
  return newList;
};
