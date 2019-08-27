import Globals
from TerrainManager import TerrainManager
from math import sin
from math import cos

from direct.actor.Actor import Actor

class TerrainTest():
	def __init__(self):
		print("TerrainTest object created")
		self.tm = TerrainManager()
		self.make_actor()
		Globals.g_task_manager.add(self.move, "moveTask")

	#test this below
	def __del__(self):
		Globals.g_task_manager.remove("moveTask")

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
		self.pc.setPos(new_x, new_y, new_z)
		#self.pc_node.setHpr(new_head, 0, 0)
		self.pc.setHpr(new_head, Globals.controls.beta, 0.0)
		return task.cont
