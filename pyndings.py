import threading
from time import sleep
from os import _exit
from sys import stdout
from traceback import format_exc
import Queue
class Pyndings(object):
	def __init__(self):
		self.thread1 = threading.Thread(target=self.run, args=())
		self.thread1.daemon = True
		self.thread2 = threading.Thread(target=self.run3, args=())
		self.thread2.daemon = True
		self.loop = True
		self.queue = Queue.Queue()
		self.aqueue = Queue.Queue()
	def run(self):
		while True:
			try:
				val = raw_input("")
				self.loop = val != "~~LOOPEND~~"
				if self.loop:
					if val[:9] == "~~ASYNC~~":
						self.aqueue.put(val[9:])
						codeth = threading.Thread(target=self.run2, args=())
						codeth.daemon = True
						codeth.start()
					else:
						self.queue.put(val)
						stdout.flush()
			except:
				print "~~ERRORS~~: " + format_exc()
				stdout.flush()
				_exit(1)
	def run2(self):
		try:
			val = self.aqueue.get(False)
			eval(compile("pynd__out = " + val + "\nprint \"~~RETURN~~: \" + str(type(pynd__out)) + \" \" + str(pynd__out)", '<string>', 'exec'), self.globe)
			stdout.flush()
		except Queue.Empty:
			self.doNothing()
		except:
			print "~~ERRORS~~: " + format_exc()
			stdout.flush()
			_exit(1)
	
	def run3(self):
		while True:
			try:
				val = self.queue.get(False)
				eval(compile("pynd__out = " + val + "\nprint \"~~RETURN~~: \" + str(type(pynd__out)) + \" \" + str(pynd__out)", '<string>', 'exec'), self.globe)
				stdout.flush()
			except Queue.Empty:
				self.doNothing()
			except:
				print "~~ERRORS~~: " + format_exc()
				stdout.flush()
				_exit(1)
		
	def doNothing(self):
		return None
	
	
	def start(self, dictionary):
		self.globe = dictionary
		self.thread1.start()
		self.thread2.start()
		while True:
			sleep(3600)
pynd = Pyndings()
def pprint(msg):
	print msg
	stdout.flush()

