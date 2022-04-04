#!/usr/bin/node
const NoO = parseInt(process.argv[2]);
if (NoO) {
  for (let x = 0; x < NoO; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
