#!/usr/bin/node

let fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (e, data) {
    if (e) {
	console.log(e);
    } else {
	console.log(data);
    }
});
