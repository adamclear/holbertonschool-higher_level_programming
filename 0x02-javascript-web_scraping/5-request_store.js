#!/usr/bin/node
const fileserver = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fileserver.createWriteStream(process.argv[3]));
