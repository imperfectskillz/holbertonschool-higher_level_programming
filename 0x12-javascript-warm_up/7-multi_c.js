#!/usr/bin/node

var i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
