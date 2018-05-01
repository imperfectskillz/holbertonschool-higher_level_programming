#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  let num = parseInt(process.argv[2]);
  console.log('My number: ' + num);
}
