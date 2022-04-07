#!/usr/bin/node
const fileserver = require('fs');
fileserver.writeFile(process.argv[2], process.argv[3],
  'utf-8', function (error, content) {
    if (error) {
      console.error(error);
    }
  });
