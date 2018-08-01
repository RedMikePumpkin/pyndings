# Pyndings
Bind python scripts to node.js

## Installation

Currently Pyndings is not available on npm so you have to clone the repository using

```
cd your/node/directory/node-modules
git clone https://github.com/RedMikePumpkin/pyndings.git
```

## Usage

to create a new python binding use

```javascript
var pyndings = require("pyndings");

var python = new pyndings("path/to/script.py");
```

## Functions

### `new pyndings(path)`

Creates a new python binding (pyding)

  - `path <string>`: path to the python file

### `pyding.onPrint(callback)`

callback for print functions

  - `callback <function>`:
    - `data <string>`: string containing printed data

### `pynding.onReturn(callback)`

callback for returned value from function

  - `callback <function>`:
    - `data <array>`:
      - `type <string>`: type of return according to python
      - `value <string>`: value of return after being put through str()

### `pynding.onError(callback)`

callback for errors

  - `callback <function>`:
    - `data <string>`: string containing error traceback

### `pynding.run(command[, async])`

runs the command

  - `command <string>`: function to run
  - `async <boolean>`: run process in seperate thread

### `pynding.stopLoops()`

makes `pynd.loop = False` until next command is sent

### `pynding.close()`

closes the python binding

## Python

to bind a python script to node.js, you need to import the pyndings library

```python
from pyndings import pynd, pprint
```

you also need to make sure that you use `pprint(msg)` instad of `print msg` and at the very end of the program have

```python
pynd.start(globals())
```

you can also use `while pynd.loop:` instead of `while True:` for loops that you want to stop by using `pynding.stopLoops()`
