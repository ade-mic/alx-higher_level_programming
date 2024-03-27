#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
// input from cmd line
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) throw error;
  else if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedCounts = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (completedCounts[todo.userId]) {
          completedCounts[todo.userId]++;
        } else {
          completedCounts[todo.userId] = 1;
        }
      }
    }
    console.log(completedCounts);
  }
});
