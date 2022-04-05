#!/usr/bin/node
const Skware = require('./5-square');

module.exports = class Square extends Skware {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let x = 0; x < this.width; x++) {
      console.log(c.repeat(this.width));
    }
  }
};
