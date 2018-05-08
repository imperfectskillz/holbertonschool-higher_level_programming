#!/usr/bin/node

exports.esrever = function (list) {
    var result = []
    for (let i = 0; i < list.length; i++) {
	result.unshift(list[i]);
    }
    return result;
}
