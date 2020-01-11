import os
import sys

from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.gui.DirectGui import DirectButton

import Globals

class MainMenu():
	def __init__(self):
		print("MainMenu object created")
		self.bk_text = "This is my Demo"
		self.textObject = OnscreenText(text = self.bk_text, pos = (0.95,-0.95),
										   scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)

		self.f = DirectFrame(frameColor=(1, 0, 0, 1), frameSize=(-1, 1, -1, 1))
		self.f.setPos(-0.5, 0, -0.5)

		self.t = DirectLabel(self.f, text="Glorious title", scale=0.1, pos=(0,0, 0.9))

		self.b = DirectButton(self.f, text = ("Exit", "click!", "rolling over", "disabled"),
								  scale=.15, pos=(0,0, 0.1), text_scale=0.5, command=self.setText)

		self.ttb = DirectButton(self.f, text=("Terrain Test"),
									scale=.15, pos=(0,0, 0.2), text_scale=0.5, command=self.request_state,
									extraArgs=["TerrainTest"])

		self.ccb = DirectButton(self.f, text=("CharGen Test"),
									scale=.15, pos=(0,0, 0.3), text_scale=0.5, command=self.request_state,
									extraArgs=["CharGen"])

	def setText(self):
		self.bk_text = "Button Clicked"
		self.textObject.setText(self.bk_text)
		self.f.destroy()
		Globals.game_states.request("None")
		sys.exit()
	def request_state(self, name):
		self.f.destroy()
		self.textObject.destroy()
		#Globals.game_states.request("TerrainTest")
		Globals.game_states.request(name)
