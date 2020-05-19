import threading

from Command import Command
from Network import Network

class KeyboardThread(threading.Thread):

	def __init__(self, input_cbk = None, name='keyboard-input-thread'):
		self.input_cbk = input_cbk
		super(KeyboardThread, self).__init__(name=name)
		self.start()

	def run(self):
		while True:
			self.input_cbk(input()) #waits to get input + Return

class ConsoleInput():
	def __init__(self, netobj = Network()):
		kthread = KeyboardThread(self.input_callback)
		self.command = Command(netobj)

	def input_callback(self, inp):
		self.command.execute(inp)
		#print('You Entered:', inp)
