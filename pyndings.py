import threading
from time import sleep
from os import _exit
from sys import stdout
from traceback import format_exc
class Pyndings(object):
	def __init__(self):
		self.thread = threading.Thread(target=self.run, args=())
		self.thread.daemon = True
	def run(self):
		while True:
			try:
				val = raw_input("")
				eval(compile("pynd__out = " + val + "\nprint \"~~RETURN~~: \" + str(type(pynd__out)) + \" \" + str(pynd__out)", '<string>', 'exec'), self.globe)
				stdout.flush()
			except:
				print "~~ERRORS~~: " + format_exc()
				stdout.flush()
				_exit(1)
	def start(self, dictionary):
		self.globe = dictionary
		self.thread.start()
		while True:
			sleep(100)
pynd = Pyndings()
def pprint(msg):
	print msg
	stdout.flush()

