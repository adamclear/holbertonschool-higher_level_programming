#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jsonResponse = JSON.parse(body).results;
    let count = 0;
    for (const movies in jsonResponse) {
      const chars = jsonResponse[movies].characters;
      for (const possibleWedges in chars) {
        if (chars[possibleWedges].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
