#!/usr/bin/node
// class Square that defines a sqaure and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle').Rectangle;

exports.Square = function Square (size) {
  Rectangle.prototype.constructor.call(this);
  this.width = size;
  this.height = size;
  this.size = size;
};