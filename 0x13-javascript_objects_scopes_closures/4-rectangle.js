#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
	if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	}
    }

    print () {
	let s = "";
	for (let i = 0; i < this.height; i++) {
	    for (let j = 0; j < this.width; j++) {
		s += "X";
	    }
	    console.log(s);
	    s = "";
	}
    }

    rotate () {
	let x = this.width;
	this.width = this.height;
	this.height = x;
    }

    double () {
	this.width *= 2;
	this.height *= 2;
    }
};

module.exports = Rectangle;
