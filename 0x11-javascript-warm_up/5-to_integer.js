#!/usr/bin/node
// Prints "My number: " if the first argument can be converted to an integer
// If the argument can't be converted to an integer, print "Not a number"

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
