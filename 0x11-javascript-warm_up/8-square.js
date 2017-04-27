#!/usr/bin/node
// Prints a square using "X", where first argument is the size of the square
// If the first argument can't be converted to an integer, print "Missing size"

if (process.argv.length < 3 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
    for (let i = 0; i < process.argv[2]; ++i) {
        console.log('X'.repeat(process.argv[2]));
    }
}
