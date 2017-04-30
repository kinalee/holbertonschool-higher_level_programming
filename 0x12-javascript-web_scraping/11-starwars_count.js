#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present

const url = 'http://swapi.co/api/films/';
const wedge = 'http://swapi.co/api/people/18/';
const request = require('request');
request(url, function (err, data) {
  if (err) {
    console.error(err);
  }
