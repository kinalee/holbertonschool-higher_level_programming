#!/usr/bin/node
// computes the number of tasks completed by user id

const todoUrl = process.argv[2];
const userUrl = 'https://jsonplaceholder.typicode.com/users'
const request = require('request');
let toDo = {};

