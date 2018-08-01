from sys import path
path.insert(0, './node_modules/pyndings/')
from pyndings import pynd, pprint
import gpiozero
from time import sleep

pins = [ # 28 pins
	None, None, None, None,
	None, None, None, None,
	None, None, None, None,
	None, None, None, None,
	None, None, None, None,
	None, None, None, None,
	None, None, None, None,
]

def pinMode(pin, mode):
	assert pin >= 0 and pin < 28
	assert mode == 1 or mode == 0
	if mode == 1:
		pins[pin] = gpiozero.Button(pin)
	else:
		pins[pin] = gpiozero.LED(pin)

def pinRead(pin):
	return pins[pin].is_pressed
	
def pinWrite(pin, value):
	assert value == 0 or value == 1
	if value == 1:
		pins[pin].on()
	else:
		pins[pin].off()

pinMode(23, 1)
pinMode(18, 0)

def buttonloop():
	pressed = False;
	while True:
		if pinRead(23):
			if not pressed:
				pressed = True
				pprint("Button pressed");
		else:
			pressed = False

def pwm(n, d):
	state = 0
	while pynd.loop:
		state = 0 if state >= d else state + 1
		pinWrite(18, 1 if state < n else 0)
	pinWrite(18, 0)

pynd.start(globals())
