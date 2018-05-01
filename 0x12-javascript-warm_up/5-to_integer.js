#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  let temp = parseInt(process.argv[2]);
  console.log('Ny number: ' + temp);
}
