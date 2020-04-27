import Globals
import Collider

from TerrainManager import TerrainManager
from Character import Character

from math import sin
from math import cos

from direct.actor.Actor import Actor

from panda3d.core import CollisionCapsule
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerEvent
from direct.showbase.DirectObject import DirectObject

from direct.task.Task import Task

quick_collisions = True

class TerrainTest(DirectObject):
	def __init__(self):
		print("TerrainTest object created")
		self.make_traverser_handler()
		self.tm = TerrainManager(16, 16)

		#self.make_actor()
		char = Character("pandabuddy")
		self.pc = char.panda_actor

		Globals.g_task_manager.add(self.move, "moveTask")
		self.task1 = Task(self.gravity)
		Globals.g_task_manager.add(self.task1, "gravityTask", extraArgs=[self.task1, self.pc])

	def __del__(self):
		print("Removed moveTask")
		Globals.g_task_manager.remove("moveTask")

	def hanev(self, col_entry):
		print("collided")

	def make_traverser_handler(self):
		base.cTrav = CollisionTraverser()
		base.mchandler = CollisionHandlerEvent()
		base.mchandler.addInPattern('into-%in')
		base.mchandler.addAgainPattern('%fn-again-%in')
		base.mchandler.addOutPattern('out-%in')

	def make_actor(self):
		self.pc_node = base.render.attachNewNode("pcnode")
		self.pc = Actor("models/panda-model", {"walk": "models/panda-walk4"})
		self.pc.setScale(0.05, 0.05, 0.05)
		self.pc_node.reparentTo(self.pc)
		self.pc.setPos(0,0,0)
		self.pc_node.setCompass()
		self.pc.reparentTo(base.render)
		base.camera.reparentTo(self.pc_node)
		base.camLens.setFar(500000000000.0)
		base.camera.setPos(0, 0, 0)

		self.make_actor_collisions(self.pc)
		self.make_test_capsule()

	def make_test_capsule(self):
		cap = CollisionCapsule(100, 100, 100, 100, 100, 100, 100)
		self.collision_node = base.render.attachNewNode(CollisionNode('cap1'))
		self.collision_node.node().addSolid(cap)
		self.collision_node.show()
		self.accept('into-cap1', self.hanev)
		self.accept('out-cap1', self.hanev)

		base.cTrav.addCollider(self.collision_node, base.mchandler)

		self.collision_node.setPos(10, 0, -3)

	def make_actor_collisions(self, actor):
		pcol = CollisionCapsule(0, 0, 0, 0, 0, 400, 400)
		self.collision_node = actor.attachNewNode(CollisionNode('pcol'))
		self.collision_node.node().addSolid(pcol)
		self.collision_node.show()
		self.collision_node.setHpr(0, 90, 0)
		self.collision_node.setPos(0, 0, 300)
		self.accept('into-pcol', self.hanev)
		self.accept('out-pcol', self.hanev)

		base.cTrav.addCollider(self.collision_node, base.mchandler)

	def move(self, task):

		#dt is the time since last frame
		dt = globalClock.get_dt()

		speed = 5.0
		new_x = self.pc.getX()
		new_y = self.pc.getY()
		new_z = self.pc.getZ()
		new_head = self.pc.getH()

		if not Globals.key_map["mouse3"]:
			self.r_x_pos = base.win.getPointer(0).getX()
			self.r_y_pos = base.win.getPointer(0).getY()


		if Globals.key_map["left"]:
			new_x -= cos(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			new_y -= sin(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			new_head = Globals.controls.alpha-90
			if Globals.key_map["forward"]: #both left and foward held
				new_head = Globals.controls.alpha-135
			elif Globals.key_map["backward"]:
				new_head = Globals.controls.alpha-45
		if Globals.key_map["right"]:
			new_x += cos(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			new_y += sin(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			if Globals.key_map["forward"]:
				new_head = Globals.controls.alpha+135
			elif Globals.key_map["backward"]:
				new_head = Globals.controls.alpha+45
			else:
				new_head = Globals.controls.alpha+90
		if Globals.key_map["forward"]:
			new_x -= sin(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			new_y += cos(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			if not Globals.key_map["right"] and not Globals.key_map["left"]:
				new_head = Globals.controls.alpha+180
		if Globals.key_map["backward"]:
			new_x += sin(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			new_y -= cos(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			if not Globals.key_map["right"] and not Globals.key_map["left"]:
				new_head = Globals.controls.alpha

		if Globals.key_map["mouse3"]:
			c_x_pos = base.win.getPointer(0).getX()
			c_y_pos = base.win.getPointer(0).getY()
			c_x_pos -= self.r_x_pos
			c_y_pos -= self.r_y_pos
			Globals.controls.alpha -= c_x_pos*0.05
			Globals.controls.beta -= c_y_pos*0.05
			base.camera.setHpr(Globals.controls.alpha, Globals.controls.beta, 0.0)
			base.win.movePointer(0, int(self.r_x_pos), int(self.r_y_pos))

			camera_dist = 3000
			camera_z_dist = 100
			#rotate camera around the node
			base.camera.setPos(sin(Globals.controls.alpha*Globals.DEG_TO_RAD)*abs(camera_dist),
								   cos(Globals.controls.alpha*Globals.DEG_TO_RAD)*-(abs(camera_dist)),
								   cos(Globals.controls.beta*Globals.DEG_TO_RAD)*camera_z_dist)


		#Set the new position and rotation
		#self.pc.setPos(new_x, new_y, new_z)

		#ele, norm = self.tm.get_terrain(0, 0).fast_cols(new_x, new_y)
		elev, norm = self.tm.get_terrain(0, 0).fast_cols(int(new_x/Globals.TERRAIN_MULT), int(new_y/Globals.TERRAIN_MULT))
		self.pc.setHpr(new_head, norm.x, 0)
		self.pc.setPos(new_x, new_y, new_z)

		cell_x = int((self.pc.getX()/4)/512)
		cell_y = int((self.pc.getY()/4)/512)

		print("POSITION: "+str(cell_x)+", "+str(cell_y))
		return(task.cont)

	def get_elevation(self, x, y):
		return(self.tm.get_terrain(0, 0).getElevation(x*Globals.TERRAIN_MULT, y*Globals.TERRAIN_MULT))

	def gravity(self, task, node):
		zpos = node.getZ()
		tcell = self.tm.get_terrain(0, 0)
		elevation = tcell.terrain.get_elevation(node.getX()/Globals.TERRAIN_MULT, node.getY()/Globals.TERRAIN_MULT)*300
		if elevation == zpos:
			1+1
		elif elevation < zpos:
		#zpos -= zpos - 1
			zpos = zpos - 1
			node.setZ(zpos)
		else:
			node.setZ(elevation)

		return(task.cont)
