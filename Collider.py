import Globals

from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerEvent
from direct.showbase.DirectObject import DirectObject

from direct.showbase.ShowBase import ShowBase


class CollisionBase(ShowBase):
	def __init__(self):
		self.cTrav = CollisionTraverser()
		self.mchandler = CollisionHandlerEvent()
		self.mchandler.addInPattern('into-%in')
		self.mchandler.addAgainPattern('%fn-again-%in')
		self.mchandler.addOutPattern('out-%in')

c = CollisionBase()
