#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
    charPrint (c) {
	if (c === undefined) {
	    this.print("X");
	} else {
	    let x = ""
	    for (let i = 0; i < this.height; i++) {
		for (let j = 0; j < this.height; j++) {
		    x += c;
		}
		console.log(x);
		x = "";
	    }
	}
    }
};

module.exports = Square;
