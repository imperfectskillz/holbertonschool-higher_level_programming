#!/usr/bin/node

function add (a, b) {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
add(process.argv[2], process.argv[3]);
