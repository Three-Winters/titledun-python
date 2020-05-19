from panda3d.core import NodePath
from direct.actor.Actor import Actor
from panda3d.physics import ActorNode
from panda3d.physics import ForceNode
from panda3d.physics import LinearVectorForce

from panda3d.core import LPoint3

import Globals

from panda3d.core import BitMask32

class Character():
	def __init__(self, name):
		self.name = name
		self.cell_x = 0
		self.cell_y = 0
		self.vel = LPoint3(0, 0, 0)

		self.c_node = base.render.attachNewNode(
			self.name+"_camera_node")


		self.panda_actor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
		self.panda_actor.setScale(0.05, 0.05, 0.05)

		self.p_node = NodePath(self.name+"_phys_node")
		self.p_node.reparentTo(render)

		self.an = ActorNode("panda-phys")
		self.anp = self.p_node.attachNewNode(self.an)
		base.enableParticles()
		base.physicsMgr.attachPhysicalNode(self.an)
		self.panda_actor.reparentTo(self.anp)

		gravityFN=ForceNode('world-forces')
		gravityFNP=render.attachNewNode(gravityFN)
		#gravityForce=LinearVectorForce(0,0,-9.81) #gravity acceleration
		self.gravityForce=LinearVectorForce(0,0,-9.81)
		gravityFN.addForce(self.gravityForce)

		base.physicsMgr.addLinearForce(self.gravityForce)


		self.c_node.reparentTo(self.panda_actor)
		self.c_node.setCompass()
		#self.panda_actor.reparentTo(base.render)
		base.camera.reparentTo(self.c_node)

		self.box = loader.loadModel("box.egg")
		self.box.setScale(100, 100, 100)
		self.box.setPos(-180, 0, 0)
		self.boxc = self.box.find("**/Cube")
		self.boxc.node().setIntoCollideMask(BitMask32.bit(0))
		self.boxc.node().setFromCollideMask(BitMask32.allOff())

		self.ban = ActorNode("box-phys")
		base.physicsMgr.attachPhysicalNode(self.ban)

		self.bp_node = NodePath(self.name+"_phys_node2")
		self.bp_node.reparentTo(render)

		self.banp = self.bp_node.attachNewNode(self.ban)
		self.box.reparentTo(self.banp)

		self.boxc.show()
		#self.box.reparentTo(base.render)

	def get_pos(self):
		return(self.panda_actor.getPos())

	def get_cell_pos(self):
		return((self.cell_x, self.cell_y))

	def set_cell_pos(self):
		self.cell_x = int((self.panda_actor.getX()/Globals.TERRAIN_MULT)/512)
		self.cell_y = int((self.panda_actor.getY()/Globals.TERRAIN_MULT)/512)

	def get_velocity(self):
		return self.vel
