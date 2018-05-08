#!/usr/bin/node

let request = require('request');

request(process.argv[2], function (error, response, body) {
    if (error) {
	console.log(error);
    }
    if (response.statusCode === 200) {
	let count = 0;
	for (let film in JSON.parse(body).results) {
	    let charac = film['characters'];
	    for (let ch in charac) {
		if (charac[ch].includes('18')) {
		    count++;
		}
	    }
	}
	console.log(count);
    }
});
