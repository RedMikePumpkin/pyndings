from pyndings import pynd, pprint
from time import sleep
import gpiozero

button = gpiozero.Button(23)

pprint("Hello, World!")

def hello_again(msg):
	pprint("hi.")
	return "hello", msg

def b():
	while True:
		button.wait_for_press()
		pprint("pressed!")
		button.wait_for_release()
		pprint("released!")

def goodbye(msg):
	pprint("bye!")
	return msg

def err():
	assert False

pynd.start(globals())
