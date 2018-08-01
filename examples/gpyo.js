var pyndings = require("pyndings");

var pynding = new pyndings("node_modules/pyndings/examples/gpyo.py");

var cycle = false;
pynding.onPrint((data) => {
	console.log(data);
	if (data === "Button pressed")
		cycle = true;
});
pynding.onReturn((data) => {
	console.log(data + " returned");
});
pynding.onError((data) => {
	throw new Error(data);
});
var int;
var val = 1;
var change = 1;
int = function() {
	if (cycle) {
		cycle = false;
		val += change;
		if (val > 4) {
			val = 3;
			change = -1;
		}
		if (val < 0) {
			val = 1;
			change = 1;
		}
		console.log(val);
		pynding.stopLoops();
		if (val !== 0)
			pynding.run("pwm(1, " + val.toString() + ")", true);
		else
			pynding.run("pwm(0, 1)", true);
	}
	setTimeout(int, 10);
}

pynding.run("buttonloop()", true);
int();
