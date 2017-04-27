#!/usr/bin/node
// Prints x times "C is fun", where x is the first argument of the script

if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(process.argv[2]); ++i) {
    console.log('C is fun');
  }
}
