from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.gui.DirectGui import DirectButton

import Globals

class CharGen():
	def __init__(self):
		self.text = "CharGen"
		self.textObject = OnscreenText(text = self.text, pos = (0.95,-0.95),
										   scale = 0.07,fg=(1,0.5,0.5,1),align=TextNode.ACenter,mayChange=1)

		self.f = DirectFrame(frameColor=(1, 1, 1, 1), frameSize=(-1, 1, -1, 1))
		self.f.setPos(-0.5, 0, -0.5)

		self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
		self.pandaActor.setScale(0.005, 0.005, 0.005)
		self.pandaActor.reparentTo(base.render)
