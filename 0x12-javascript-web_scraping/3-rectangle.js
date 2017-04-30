#!/usr/bin/node
// class Rectangle that defines a rectangle
// The constructor must take 2 arguments w and h

exports.Rectangle = function Rectangle (w, h) {
  // Initialize the instance attribute width with the value of w
  // Initialize the instance attribute height with the value of h
  // If w or h is equal to 0 or not a positive integer, create an empty object
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  // Create an instance method called print() that prints the rectangle using the character X
  this.print = function () {
    for (var i = 0; i < this.height; ++i) {
      console.log('X'.repeat(this.width));
    }
  };
};