import Globals
from TerrainManager import TerrainManager

class TerrainTest():
	def __init__(self):
		print("TerrainTest object created")
		self.tm = TerrainManager()
		Globals.g_task_manager.add(self.move, "moveTask")

	#test this below
	def __del__(self):
		Globals.g_task_manager.remove("moveTask")

	def move(self, task):

		#dt is the time since last frame
		dt = globalClock.get_dt()

		if Globals.key_map["left"]:
			Globals.camera.setX(Globals.camera.getX() - 5.0)
		if Globals.key_map["right"]:
			Globals.camera.setX(Globals.camera.getX() + 5.0)
		if Globals.key_map["forward"]:
			Globals.camera.setZ(Globals.camera.getZ() + 5.0)
		if Globals.key_map["backward"]:
			Globals.camera.setZ(Globals.camera.getZ() - 5.0)
		if Globals.key_map["mouse3"]:
			c_x_pos = Globals.win.getPointer(0).getX()
			c_y_pos = Globals.win.getPointer(0).getY()
			c_x_pos -= self.r_x_pos
			c_y_pos -= self.r_y_pos
			Globals.controls.alpha -= c_x_pos * 0.05
			Globals.controls.beta -= c_y_pos * 0.05
			Globals.camera.setHpr(Globals.controls.alpha, Globals.controls.beta, 0.0)
			Globals.win.movePointer(0, int(self.r_x_pos), int(self.r_y_pos))
		if not Globals.key_map["mouse3"]:
			self.r_x_pos = Globals.win.getPointer(0).getX()
			self.r_y_pos = Globals.win.getPointer(0).getY()
		return task.cont
