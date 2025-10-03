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

if (args === undefined) {
	console.log('Not a number');
} else {
	const number = parseInt(args);

	if (isNaN(number)) {
		console.log('Not a number');
	} else {
		console.log(`My  number: ${number}`);
	}

}


