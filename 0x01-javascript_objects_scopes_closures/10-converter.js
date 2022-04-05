#!/usr/bin/node
exports.converter = function (base) {
  return function converted (num) {
    return num.toString(base);
  };
};
