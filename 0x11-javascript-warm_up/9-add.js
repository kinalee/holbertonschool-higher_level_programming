#!/usr/bin/node
// Function that prints the addition of 2 integers
// The first argument is the first integer
// The second argument is the second integer

function add(a, b) {
  console.log(a + b);
}

add(Number(process.argv[2]), Number(process.argv[3]));
