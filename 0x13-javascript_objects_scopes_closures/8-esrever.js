#!/usr/bin/node

exports.esrever = function (list) {
    let result = []
    for (let i = 0; i < list.length; i++) {
	result.unshift(list[i]);
    }
    return result;
}
