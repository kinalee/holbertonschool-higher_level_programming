#!/usr/bin/node
// displays the status code of a GET request.

const url = process.argv[2];
var request = require('request');
request(url, function (err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
