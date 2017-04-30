#!/usr/bin/node
// class Rectangle that defines a rectangle:
// The constructor must take 2 arguments w and h

exports.Rectangle = function Rectangle (w, h) {
  // Initialize the instance attribute width with the value of w
  // Initialize the instance attribute height with the value of h
  // If w or h is equal to 0 or not a positive integer, create an empty object
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  // Instance method called print() that prints the rectangle using the character X
  this.print = function () {
    for (let i = 0; i < this.height; ++i) {
      console.log('X'.repeat(this.width));
    }
  };
  // Instance method called rotate() that exchanges the width and the height of the rectangle
  this.rotate = function () {
    [this.width, this.height] = [this.height, this.width];
  };
  // Instance method called double() that multiples the width and the height of the rectangle by 2

  this.double = function () {
    this.width *= 2;
    this.height *= 2;
  };
};
