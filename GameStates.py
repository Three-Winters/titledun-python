from direct.fsm.FSM import FSM

from State import State
from MainMenu import MainMenu
from TerrainTest import TerrainTest
from CharGen import CharGen

class GameStates(FSM):
	def __init__(self):
		FSM.__init__(self, "GameStates")
		self.registry = {}

	def register_state(self, fun, name):
		self.registry[name] = State(fun, name)

	def unregister_state(self, name):
		try:
			self.registry.pop(name)
		except NameError:
			print("State not found "+name)

	def request_enter(self, name):
		self.registry[name].enter()

	def request_exit(self):
		self.registry[name].exit()

	# -- To Remove
	def enterMainMenu(self):
		self.mm = MainMenu()
		print("Main menu entered")
	def exitMainMenu(self):
		#self.mm = None
		del self.mm
		print("Main menu exited")

	def enterTerrainTest(self):
		self.tt = TerrainTest()
		print("TerrainTest entered")
	def exitTerrainTest(self):
		del self.tt
		print("TerrainTest exited")

	def enterCharGen(self):
		self.cc = CharGen()
		print("CharGen entered")
	def exitCharGen(self):
		del self.cc
		print("CharGen exited")
