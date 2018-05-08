#!/usr/bin/node

let fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (e, data) {
    if (e) {
	console.log(e);
    }
});
