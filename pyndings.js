var spawn = require("child_process").spawn;

class python {
	constructor (path) {
		this.path = path;
		this.print = function() {};
		this.return = function() {};
		this.error = function() {};
		this.py = spawn("python", [path]);
		this.py.stdin.setEncoding("utf-8");
		this.py.stdout.emitToPython = function(name, data) {
			_this[name](data);
		}
		var _this = this;
		this.py.stdout.on('data', function(d) {
			console.log("o");
			var data = d.toString();
			var ss = data.substring(0, 12);
			var sp = data.slice(12, -1);
			if (ss === "~~RETURN~~: ") {
				var type = sp.split(" ")[1];
				type = type.slice(0, -1);
				var val = sp.split(" ");
				val = val.slice(2, val.length).join("");
				this.emitToPython("return", [type, val]);
			} else if (ss === "~~ERRORS~~: ") {
				this.emitToPython("error", sp);
			} else {
				this.emitToPython("print", data.trim());
			}
		});
	}
	
	run (command) {
		this.py.stdin.write(command + "\n");
	}
	
	close () {
		this.py.kill("SIGINT");
	}
	
	onPrint (callback) {
		this.print = callback;
	}
	
	onReturn (callback) {
		this.return = callback;
	}
	
	onError (callback) {
		this.error = callback;
	}
}

module.exports = python;
