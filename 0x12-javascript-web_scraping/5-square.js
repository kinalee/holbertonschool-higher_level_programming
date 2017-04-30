#!/usr/bin/node
// class Square that defines a sqaure and inherits from Rectangle of 4-rectangle.js

exports.Square = function Square (size) {
  const Rectangle = require('./4-rectangle').Rectangle;
  Rectangle.call(this);
  this.width = size;
  this.height = size;
};
