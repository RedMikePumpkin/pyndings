var pyndings = require("pyndings");

var pynding = new pyndings("node_modules/pyndings/examples/helloworld.py");
pynding.onPrint((data) => {
	console.log(data);
});
pynding.onReturn((data) => {
	console.log(data + " returned");
});
pynding.onError((data) => {
	throw new Error(data);
});

setTimeout(() => {
	pynding.run("hello_again(\"Bob\")");
	pynding.run("hello_again(\"Jane\")");
	pynding.run("hello_again(\"Max\")");
	setTimeout(() => {
		pynding.run("goodbye(\"Bob\")");
		pynding.run("goodbye(\"Jane\")");
		pynding.run("goodbye(\"Max\")");
		setTimeout(() => {
			pynding.run("err()");
		}, 2000);
	}, 2000);
}, 2000);
