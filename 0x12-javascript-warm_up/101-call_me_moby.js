#!/usr/bin/node
exports.callMeMoby = function (xtimes, func) {
  while (xtimes > 0) {
    func();
    xtimes--;
  }
};
