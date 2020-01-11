from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.gui.DirectGui import DirectButton
from direct.gui.DirectGui import *

import Globals

class CharGen():
	def __init__(self):
		self.text = "CharGen"
		self.textObject = OnscreenText(text = self.text, pos = (0.95,-0.95),
										   scale = 0.07,fg=(1, 0.5, 0.5, 1),align=TextNode.ACenter,mayChange=1)

		self.f = DirectFrame(frameColor=(1, 1, 1, 0.5), frameSize=(-1, 1, -0.4, 0.4))
		self.f.setPos(-0.5, 0, -0.5)

		self.flavorText = OnscreenText("Primary Colour",pos=(0,0,0.4),scale=0.07,align=TextNode.ACenter,mayChange=1,
										   fg=(1,1,1,1))
		self.flavorText.reparent_to(self.f)
		self.flavorText.setPos(0, 0.2)
		#slider R
		self.sR = DirectSlider(self.f, range=(0,1), value=0, pageSize=3, command=self.setCol)
		self.sR.setScale(0.5, 0.5, 0.5)
		self.sR.setPos(0,0,0)
		self.sR.setColor(1,0,0)

		#slider G
		self.sG = DirectSlider(self.f, range=(0,1), value=0, pageSize=3, command=self.setCol)
		self.sG.setScale(0.5, 0.5, 0.5)
		self.sG.setPos(0,0,-0.1)
		self.sG.setColor(0,1,0)

		#slider B
		self.sB = DirectSlider(self.f, range=(0,1), value=0, pageSize=3, command=self.setCol)
		self.sB.setScale(0.5, 0.5, 0.5)
		self.sB.setPos(0,0,-0.2)
		self.sB.setColor(0,0,1)

		self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
		self.pandaActor.setScale(0.005, 0.005, 0.005)
		self.pandaActor.setPos(0.8, 12, -0.5)
		self.pandaActor.reparentTo(base.render)

	def setCol(self):
		#print(self.s['value'])
		self.pandaActor.setColor(self.sR['value'], self.sG['value'], self.sB['value'])
