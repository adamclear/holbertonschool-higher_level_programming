#!/usr/bin/node
exports.esrever = function (list) {
  let y = list.length - 1;
  const revlist = [];
  for (let x = 0; x < list.length; x++) {
    revlist[x] = list[y];
    y--;
  }
  return revlist;
};
