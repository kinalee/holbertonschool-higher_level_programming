#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square

const Square0 = require('./5-square').Square;

exports.Square = function Square (size) {
  if (size > 0) {
    Square0.call(this, size);
    this.size = size;
  }
  // Instance method called charPrint(c) that prints the rectangle using the character c
  // If c is undefined, use the character X
  Square.prototype.charPrint = function (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; ++i) {
      console.log(c.repeat(this.size));
    }
  };
};
