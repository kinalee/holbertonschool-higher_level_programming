#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer

const url = 'http://swapi.co/api/films/' + process.argv[2];
const request = require('request');

request(url, function (err, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body.body)['title']);
  }
});
