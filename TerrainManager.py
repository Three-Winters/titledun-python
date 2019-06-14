from panda3d.core import GeoMipTerrain
from TerrainCell import TerrainCell
import Globals

class TerrainManager:
	def __init__(self, render):
		self.test_texture = base.loader.loadTexture("grass.jpg")
		#intialise terrain list to zeroes!
		self.terrain_list = [[0 for x in range(16)] for y in range(16)]

		tc = TerrainCell("test1", "field.png","grass.jpg", 0, 0)
		tc.terrain.getRoot().reparentTo(render)
		self.terrain_list[0][0] = tc

		tc = TerrainCell("test2", "field.png","grass.jpg", 1, 0)
		tc.terrain.getRoot().reparentTo(render)
		self.terrain_list[1][0] = tc

		base.taskMgr.add(self.updateTask, "update")

	def updateTask(self, task):
		for i in range(len(self.terrain_list)):
			for j in range(len(self.terrain_list[i])):
				if self.terrain_list[i][j]:
					self.terrain_list[i][j].terrain.update()
		return task.cont
