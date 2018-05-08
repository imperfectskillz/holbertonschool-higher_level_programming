#!/usr/bin/node

let request = require('request');

request(process.argv[2], function (error, response, body) {
    if (error) {
	console.log(error);
    } else {
	let result = {};
	let scraped = JSON.parse(body);
	for (let each in scraped) {
	    let current = scraped[each];
	    let userid = current['userId'];
	    if (current['completed'] === true &&
		result[userid] === undefined) {
		result[userid] = 1;
	    } else if (current['completed'] === true) {
		result[userid]++;
	    }
	}
	console.log(result);
    }
});
