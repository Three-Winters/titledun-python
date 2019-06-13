from direct.fsm.FSM import FSM
from MainMenu import MainMenu
from TerrainTest import TerrainTest

class GameStates(FSM):
	def __init__(self):
		FSM.__init__(self, "GameStates")

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
