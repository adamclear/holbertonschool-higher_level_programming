#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const compDict = {};
    const jsonResponse = JSON.parse(body);
    for (let x = 0; x < jsonResponse.length; x++) {
      const id = jsonResponse[x].userId;
      const complete = jsonResponse[x].completed;
      if (complete) {
        if (!compDict[id]) {
          compDict[jsonResponse[x].userId] = 1;
        } else {
          compDict[jsonResponse[x].userId] += 1;
        }
      }
    }
    console.log(compDict);
  }
});
