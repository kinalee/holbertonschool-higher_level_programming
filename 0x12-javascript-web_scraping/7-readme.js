#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, function (err, data) {
  if (err) {
      console.log(err);
  } else {
    console.log(String(data).replace('\n', ''));
   }
});
