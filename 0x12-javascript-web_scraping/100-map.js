#!/usr/bin/node
// imports an array and computes a new array

const req = require('./100-data').list;

console.log(req);
console.log(req.map(function (num) {
  return num * parseInt(req.indexOf(num));
}));
