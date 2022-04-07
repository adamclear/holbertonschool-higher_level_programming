#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jsonResponse = JSON.parse(body);
    console.log(jsonResponse.title);
  }
});
