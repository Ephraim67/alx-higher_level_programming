#!/usr/bin/node

const args = process.argv;

if (args.lenght < 4) {
	console.log('Usage: <arg1> is <arg2>');
} else {
	const arg1 = args[2];
	const arg2 = args[3];

	console.log(`${arg1} is ${arg2}`);
}
