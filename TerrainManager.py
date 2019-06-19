from panda3d.core import GeoMipTerrain
from TerrainCell import TerrainCell
import Globals
import json

class TerrainManager:
	def __init__(self):
		self.test_texture = base.loader.loadTexture("grass.jpg")
		#intialise terrain list to zeroes!
		self.terrain_list = [[0 for x in range(16)] for y in range(16)]

		self.make_cell("0-0", "field.png", "grass.jpg", 0, 0)
		self.make_cell("0-1", "field.png", "grass.jpg", 0, 1)
		self.make_cell("0-2", "field.png", "grass.jpg", 0, 2)
		self.make_cell_json("1-0")
		self.make_cell("1-1", "field.png", "grass.jpg", 1, 1)
		self.make_cell("1-2", "field.png", "grass.jpg", 1, 2)
		self.make_cell("2-0", "field.png", "grass.jpg", 2, 0)
		self.make_cell("2-1", "field.png", "grass.jpg", 2, 1)
		self.make_cell("2-2", "field.png", "grass.jpg", 2, 2)

		base.taskMgr.add(self.updateTask, "update")

	def updateTask(self, task):
		for i in range(len(self.terrain_list)):
			for j in range(len(self.terrain_list[i])):
				if self.terrain_list[i][j]:
					self.terrain_list[i][j].terrain.update()
		return task.cont

	def dump_to_dic(self):
		terrain_settings = {}
		for i in range(len(self.terrain_list)):
			for j in range(len(self.terrain_list[i])):
				if self.terrain_list[i][j]:
					terrain_settings[self.terrain_list[i][j].settings["name"]] \
					  = self.terrain_list[i][j].settings
		return(terrain_settings)

	def dump_to_json(self, dic):
		with open("terrains.json", "w") as write_file:
			json.dump(dic, write_file, indent=4)

	def dump_terrains_json(self):
		self.dump_to_json(self.dump_to_dic())

	def make_cell(self, name, heightmap, texture, posx, posy):
		tc = TerrainCell()
		tc.configure(name, heightmap, texture, posx, posy)
		tc.create()
		tc.terrain.getRoot().reparentTo(base.render)
		self.terrain_list[posx][posy] = tc

	def make_cell_json(self, name):
		tc = TerrainCell()
		if tc.json_decode(name) == True:
			tc.create()
			tc.terrain.getRoot().reparentTo(base.render)
			self.terrain_list[tc.settings["x"]][tc.settings["y"]] = tc
