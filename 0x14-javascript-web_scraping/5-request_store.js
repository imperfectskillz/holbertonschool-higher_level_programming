#!/usr/bin/node

let fs = require('fs');
let request = require('request');

request(process.argv[2], function (error, response, body) {
    if (error) {
	console.log(error);
    } else {
	fs.writeFile(process.argv[3], body, 'utf-8');
    }
});
