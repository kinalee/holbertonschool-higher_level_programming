#!/usr/bin/node
// Prints two arguments passed to it, in the following format:
// "first argument is second argument"

if (!process.argv[2]) {
  console.log(typeof process.argv[2] + ' is ' + typeof process.argv[2]);
} else if (!process.argv[3]) {
  console.log(process.argv[2] + ' is ' + typeof process.argv[3]);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
