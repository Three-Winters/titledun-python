import Globals
import Collider

from TerrainManager import TerrainManager
from Character import Character

from math import sin
from math import cos

from direct.actor.Actor import Actor

from panda3d.core import LPoint3

from panda3d.core import CollisionCapsule
from panda3d.core import CollisionSphere
from panda3d.core import CollisionNode
from panda3d.core import CollisionPolygon
from panda3d.core import CollisionPlane
from panda3d.core import CollisionRay
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerEvent
from panda3d.core import CollisionHandlerPusher
from panda3d.physics import PhysicsCollisionHandler
from direct.showbase.DirectObject import DirectObject
from panda3d.physics import ActorNode
from panda3d.core import LVector3f
from panda3d.core import LPlane
from direct.task.Task import Task

quick_collisions = True

from panda3d.core import BitMask32
class TerrainTest(DirectObject):
	def __init__(self):
		print("TerrainTest object created")
		self.make_traverser_handler()
		self.tm = TerrainManager(16, 16)

		self.down = 0

		self.PCs = {}

		#self.make_actor()
		self.char = Character("pandabuddy")
		self.pc = self.char.panda_actor
		self.make_actor_collisions(self.pc)
		#self.make_test_capsule()
		self.tm.get_terrain(0, 0).terrain.getRoot().setTag('myObjectTag', '1')

		#self.tm.get_terrain(0, 0).terrain.getRoot().setIntoCollideMask(BitMask32.bit(0))
		#col_t = CollisionNode("col_t")
		#col_t.addSolid(CollisionPolygon(self.tm.get_terrain(0, 0).terrain.getRoot()))
		#CollisionPolygon(self.tm.get_terrain(0, 0).terrain.getRoot())
		#base.cTrav.addCollider(self.tm.get_terrain(0, 0).terrain.getRoot(), base.mchandler)

		#pusher = CollisionHandlerPusher()
		#pusher.addCollider(self.collision_node, self.char.boxc)
		#base.cTrav.addCollider(self.collision_node, pusher)

		#base.cTrav.addCollider(self.collision_node, base.mchandler)

		cp = CollisionPlane(LPlane((0,0,1), (0,0,0)))
		#self.planeANP = render.attachNewNode(ActorNode('p actor'))
		planeNP = base.render.attachNewNode(CollisionNode('planecnode'))
		#planeNP = self.planeANP.attachNewNode(CollisionNode('planecnode'))
		self.accept('into-planecnode', self.hanev)
		self.accept('pcol-again-planecnode', self.hanev)
		planeNP.node().addSolid(cp)
		planeNP.show()
		planeNP.setScale(100, 100, 100)
		planeNP.node().setIntoCollideMask(BitMask32.bit(0))
		planeNP.node().setFromCollideMask(BitMask32.allOff())
		planeNP.setPos(0,0,-100)
		#base.mchandler.addCollider(planeNP, self.planeANP)
		#base.cTrav.addCollider(planeNP, base.mchandler)
		#base.physicsMgr.attachPhysicalNode(self.planeANP.node())

		base.cTrav.addCollider(self.char.boxc, base.mchandler)
		base.cTrav.setRespectPrevTransform(True)

		#base.mchandler.addCollider(self.collision_node, self.char.panda_actor)
		#base.mchandler.addCollider(self.collision_node, self.char.boxc)
		#base.mchandler.addCollider(self.char.boxc, self.collision_node)
		Globals.g_task_manager.add(self.move, "moveTask", priority=-100)
		self.task1 = Task(self.gravity)
		Globals.g_task_manager.add(self.task1, "gravityTask", extraArgs=[self.task1, self.pc])

	def __del__(self):
		print("Removed moveTask")
		Globals.g_task_manager.remove("moveTask")

	def hanev(self, col_entry):
		#print("collided: "+str(col_entry)) #panda3d.core.CollisionEntry
		#self.char.boxc.setPos(0,0,0)
		#print("old pos: "+str(self.pos)+"\nnew pos: "+str(self.pc.getPos()))

		#self.pc.setPos(self.pos+self.vel)#*1.01)
		#self.char.an.getPhysicsObject().addImpulse(self.pos+self.vel)
		#self.char.vel = LPoint3(0, 0, 0)

		#self.char.an.getPhysicsObject().setVelocity((-(self.char.an.getPhysicsObject().getVelocity().getX()*1.0),
		#												 -(self.char.an.getPhysicsObject().getVelocity().getY()*1.0),
		#												 0))#-(self.char.an.getPhysicsObject().getVelocity().getZ())))
		#self.char.an.getPhysicsObject().setVelocity(0, 0, self.char.an.getPhysicsObject().getVelocity().getZ())

		self.char.an.getPhysicsObject().setVelocity(((self.char.an.getPhysicsObject().getVelocity().getX()*1.0),
														 (self.char.an.getPhysicsObject().getVelocity().getY()*1.0),
														 0))
		#self.char.an.getPhysicsObject().addImpulse((0,0, -(self.char.an.getPhysicsObject().getVelocity().getZ()*1.0)))
		self.char.vel = self.char.an.getPhysicsObject().getVelocity()

		print("PCPOS: "+str(self.char.anp.getPos()))
		depth = col_entry.getInteriorPoint(col_entry.getIntoNodePath()).getZ()*100
		self.char.anp.setPos(self.char.anp.getPos().getX(), self.char.anp.getPos().getY(), self.char.anp.getPos().getZ()-(depth))
		lowest_z = col_entry.getContactPos(col_entry.getFromNodePath()).getZ()
		#if lowest_z > self.char.panda_actor.getPos().getZ():
			#self.char.gravityForce.setVector(0,0,0)
		#	self.char.panda_actor.setPos(self.char.panda_actor.getPos().getX(), self.char.panda_actor.getPos().getY(), lowest_z)
		#self.pc.setFluidPos(self.pos-(self.pos - self.pc.getPos()))
		#print("{ "+str(col_entry.getInteriorPoint(col_entry.getFromNodePath()))+" }")
		#self.pc.setFluidPos(self.pos-(self.pos.getX(), self.pos.getY(), -100))


	def make_traverser_handler(self):
		base.cTrav = CollisionTraverser()
		#base.mchandler = CollisionHandlerEvent()
		#base.mchandler = CollisionHandlerPusher()
		base.mchandler = PhysicsCollisionHandler()
		base.mchandler.addInPattern('into-%in')
		base.mchandler.addAgainPattern('%fn-again-%in')
		base.mchandler.addOutPattern('out-%in')
		base.mchandler.setStaticFrictionCoef(0.91)
		base.mchandler.setDynamicFrictionCoef(0.91)

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

		self.collision_node.setPos(10, 0, 81)

	def make_actor_collisions(self, actor):
		pcol = CollisionSphere(0, 400)
		self.collision_node = actor.attachNewNode(CollisionNode('pcol'))
		self.collision_node.node().addSolid(pcol)
		self.collision_node.show()
		#self.collision_node.setHpr(0, 90, 0)
		#self.collision_node.setPos(0, 0, 0)

		self.ray = CollisionRay(LPoint3(0,0,-500), LVector3f(0,0,-90))
		self.ray_node = self.char.c_node.attachNewNode(CollisionNode('pray'))
		self.ray_node.reparentTo(self.char.c_node)
		self.ray_node.node().addSolid(self.ray)
		self.ray_node.show()
		self.accept('into-pray', self.hanev)
		self.accept('Cube-again-pray', self.hanev)
		self.accept('pray-again-planecnode', self.hanev)
		self.accept('out-pray', self.hanev)
		#base.cTrav.addCollider(self.ray_node, base.mchandler)
		#base.mchandler.addCollider(self.ray_node, self.ray_node)

		self.accept('into-pcol', self.hanev)
		self.accept('Cube-again-pcol', self.hanev)
		self.accept('pcol-again-Cube', self.hanev)
		self.accept('out-pcol', self.hanev)

		self.accept('into-Cube', self.hanev)
		self.accept('again-Cube', self.hanev)
		a_pcol = ActorNode("a_pcol")
		np_pcol = self.collision_node.attachNewNode(a_pcol)
		base.physicsMgr.attachPhysicalNode(a_pcol)
		base.cTrav.addCollider(np_pcol, base.mchandler)

		base.mchandler.addCollider(self.collision_node, np_pcol)
		base.cTrav.addCollider(self.collision_node, base.mchandler)

		self.char.an.getPhysicsObject().setTerminalVelocity(0.00000001)
		self.char.an.getPhysicsObject().setOriented(True)
		self.boo = 0

	def move(self, task):
		self.pos = self.pc.getPos()

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


		if Globals.key_map["left"] == 1:
			new_x -= cos(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			new_y -= sin(Globals.DEG_TO_RAD*Globals.controls.alpha)*speed
			new_head = Globals.controls.alpha-90
			base.cTrav.traverse(base.render)
			if True:#not self.down:
				self.down = 1
				vel_add = LPoint3(new_x*10, new_y*10, self.char.an.getPhysicsObject().getVelocity().getZ())
				self.char.vel = vel_add#self.char.vel + vel_add
				self.char.vel.setZ(self.char.an.getPhysicsObject().getVelocity().getZ())
				self.char.an.getPhysicsObject().setVelocity(self.char.vel)
		if Globals.key_map["left"] == 2:
			self.down = 0
			self.char.an.getPhysicsObject().setVelocity(0, 0, self.char.an.getPhysicsObject().getVelocity().getZ())

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
			camera_z_dist = 1000
			#rotate camera around the node
			base.camera.setPos(sin(Globals.controls.alpha*Globals.DEG_TO_RAD)*abs(camera_dist),
								   cos(Globals.controls.alpha*Globals.DEG_TO_RAD)*-(abs(camera_dist)),
								   cos(Globals.controls.beta*Globals.DEG_TO_RAD)*camera_z_dist)


		#Set the new position and rotation
		#self.pc.setPos(new_x, new_y, new_z)

		#ele, norm = self.tm.get_terrain(0, 0).fast_cols(new_x, new_y)
		elev, norm = self.tm.get_terrain(0, 0).fast_cols(int(new_x/Globals.TERRAIN_MULT), int(new_y/Globals.TERRAIN_MULT))
		self.pc.setHpr(new_head, norm.x, 0)
		#self.pc.setPos(new_x, new_y, new_z)
		#self.pos = self.pc.getPos()

		self.char.set_cell_pos()
		cell_x = self.char.cell_x #int((self.pc.getX()/4)/512)
		cell_y = self.char.cell_y #int((self.pc.getY()/4)/512)

		#print("POSITION: "+str(cell_x)+", "+str(cell_y))
		self.vel = self.pos - self.pc.getPos()
		#self.pc.setPos(self.pc.getPos()+self.vel)

		#self.char.vel = LPoint3(0, 0, 0)
		#self.char.an.getPhysicsObject().setVelocity((0, 0, self.char.an.getPhysicsObject().getVelocity().getZ()))

		return(task.cont)

	def get_elevation(self, x, y):
		return(self.tm.get_terrain(0, 0).getElevation(x*Globals.TERRAIN_MULT, y*Globals.TERRAIN_MULT))

	def gravity(self, task, node):
		"""
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
			"""
		base.cTrav.traverse(render)
		return(task.cont)
