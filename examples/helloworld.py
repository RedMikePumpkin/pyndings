from pyndings import pynd, pprint

pprint("Hello, World!")

def hello_again(msg):
	pprint("hi.")
	return "hello", msg

def goodbye(msg):
	pprint("bye!")
	return msg

def err():
	assert False

pynd.start(globals())
