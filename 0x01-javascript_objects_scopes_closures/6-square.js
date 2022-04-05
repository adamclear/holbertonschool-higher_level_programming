#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let x = 0; x < this.width; x++) {
      console.log(c.repeat(this.width));
    }
  }
};
