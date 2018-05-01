#!/usr/bin/node

let temp = parseInt(process.argv[2]);
if (isNaN(temp))
{
    console.log("Not a number");
}
else
{
    console.log("Ny number: " + temp);
}
