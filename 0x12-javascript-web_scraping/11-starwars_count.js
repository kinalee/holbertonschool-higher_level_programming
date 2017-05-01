#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present

const url = process.argv[2];
const wedge = 'http://swapi.co/api/people/18/';
const request = require('request');
request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
      let count = 0;
      for (let data of JSON.parse(body.body)['results']) {
        for (let w of data['characters']) {
          if (w == wedge) {
            ++count;
          }
        }
      }
    console.log(count);
    }
});
