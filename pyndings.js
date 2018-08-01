var spawn = require("child_process").spawn,
	EventEmitter = require('events');

class python {
	constructor (path, options = {py3: false}) {
		this.path = path;
		this._emitter = new EventEmitter();
		this.py = spawn("python" + options.py3 ? "3" : "", [path]);
		this.py.stdin.setEncoding("utf-8");
		this.py.stdout.emitToPython = function(name, data) {
			_this._emitter.emit(name, data)
		}
		var _this = this;
		this.py.stdout.on('data', function(d) {
			var data = d.toString();
			var ss = data.substring(0, 12);
			var sp = data.slice(12, -1)
			if (ss === "~~RETURN~~: ") {
				var type = sp.split(" ")[1];
				type = type.slice(0, -1);
				var val = sp.split(" ")
				val = val.slice(2, val.length).join("");
				this.emitToPython("return", [type, val]);
			} else if (ss === "~~ERRORS~~: ") {
				this.emitToPython("error", sp);
			} else {
				console.log(this == py.py.stdout)
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
		this._emitter.on("print", callback);
	}
	
	onReturn (callback) {
		this._emitter.on("return", callback);
	}
	
	onError (callback) {
		this._emitter.on("error", callback);
	}
}

module.exports = python;
