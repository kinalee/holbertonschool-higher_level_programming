#!/usr/bin/node
// computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');

request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    let toDo = {};
    let data = JSON.parse(body.body);
    for (let i = 0; i < data.length; ++i) {
      if (data[i]['completed'] === true) {
        if (toDo.hasOwnProperty(data[i]['userId'])) {
          toDo[data[i]['userId']] += 1;
        } else {
          toDo[data[i]['userId']] = 1;
        }
      }
    }
    console.log(toDo);
  }
});
