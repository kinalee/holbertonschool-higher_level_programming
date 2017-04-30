#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, body.body, function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
