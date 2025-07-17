#!/usr/bin/node

/*
 * process.argv is an array that contains all command-line arguments
 *
 * process.argv.length gives the total number of items in the array
 *
 */

const args = process.argv.length - 2;

if (args === 0) {
	console.log("No argument");
} else if (args === 1) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
