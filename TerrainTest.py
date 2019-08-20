import Globals
from TerrainManager import TerrainManager

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
		self.pc = Actor("models/panda-model", {"walk": "models/panda-walk4"})
		self.pc.setScale(0.005, 0.005, 0.005)
		self.pc.reparentTo(base.render)
		self.pc.setPos(0,0,0)
		base.camera.reparentTo(self.pc)

	def move(self, task):

		#dt is the time since last frame
		dt = globalClock.get_dt()

		if Globals.key_map["left"]:
			base.camera.setX(self.pc.getX() - 5.0)
		if Globals.key_map["right"]:
			base.camera.setX(self.pc.getX() + 5.0)
		if Globals.key_map["forward"]:
			base.camera.setZ(self.pc.getZ() + 5.0)
		if Globals.key_map["backward"]:
			base.camera.setZ(self.pc.getZ() - 5.0)

		if Globals.key_map["mouse3"]:
			c_x_pos = base.win.getPointer(0).getX()
			c_y_pos = base.win.getPointer(0).getY()
			c_x_pos -= self.r_x_pos
			c_y_pos -= self.r_y_pos
			Globals.controls.alpha -= c_x_pos * 0.05
			Globals.controls.beta -= c_y_pos * 0.05
			base.camera.setHpr(Globals.controls.alpha, Globals.controls.beta, 0.0)
			base.win.movePointer(0, int(self.r_x_pos), int(self.r_y_pos))

			#rotate camera around the node
			base.camera.setPos(self.pc, sin(Globals.controls.alpha*Globals.DEG_TO_RAD*3),
								   cos(Globals.controls.alpha*Globals.DEG_TO_RAD*-3),
								   cos(Globals.controls.beta*Globals.DEG_TO_RAD))

		if not Globals.key_map["mouse3"]:
			self.r_x_pos = base.win.getPointer(0).getX()
			self.r_y_pos = base.win.getPointer(0).getY()
		return task.cont
