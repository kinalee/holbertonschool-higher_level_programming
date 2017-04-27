#!/usr/bin/node
// Computes and prints a factorial
// Factorial of NaN is 1

function factorial (num) {
  function factHelper (num) {
    if (num === 0 || isNaN(num)) {
      return 1;
    } else {
      return num * factHelper(num - 1);
    }
  }
  console.log(factHelper(num));
}

factorial(Number(process.argv[2]));
