from direct.fsm.FSM import FSM
from MainMenu import MainMenu

class GameStates(FSM):
	def __init__(self):
		FSM.__init__(self, "GameStates")

	def enterMainMenu(self):
		mm = MainMenu()
		print("Main menu entered")

	def exitMainMenu(self):
		print("Main menu exited")
