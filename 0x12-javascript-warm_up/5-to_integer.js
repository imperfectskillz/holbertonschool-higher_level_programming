#!/usr/bin/node

let num = process.argv[2];

if (isNaN(num)) {
  console.log('Not a number');
} else {
  let num = parseInt(process.argv[2]);
  console.log('Ny number: ' + num);
}
