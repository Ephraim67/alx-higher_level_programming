#!/usr/bin/node

/**
 *
 * a script that prints My number: <first argument converted in integer>
 *
 * if the first argument can be converted to an integer
 *
 * If the argument can’t be converted to an integer, print “Not a number”
 */

const args = process.argv[2];
if (isNaN(args)) {
	console.log('Not a number');
} else {
	console.log(`My number: ${args}`);
}


