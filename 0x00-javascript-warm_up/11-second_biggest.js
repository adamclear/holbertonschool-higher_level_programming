#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = process.argv.splice(2);
  array.sort(function (a, b) {
    return a - b;
  });
  console.log(array[array.length - 2]);
}
