#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js

exports.Square = function Square (size) {
  const Square0 = require('./5-square').Square;
  Square0.call(this);
  this.size = size;

  // Instance method called charPrint(c) that prints the rectangle using the character c
  // If c is undefined, use the character X
  Square.prototype.charPrint = function (c) {
    if (!c) {
      c = 'X';
    }
    for (var i = 0; i < size; ++i) {
      console.log(c.repeat(this.size));
    }
  };
};