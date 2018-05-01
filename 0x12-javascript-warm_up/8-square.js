#!/usr/bin/node

var i;
var j;

if (process.argv[2])
{
    for (i = 0; i < process.argv[2]; i++)
    {
	console.log('X'.repeat(process.argv[2]));
    }
}
else {
    console.log("Missing size");
}
