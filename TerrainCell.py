from panda3d.core import GeoMipTerrain

import Globals

import json

class TerrainCell:
	def __init__(self):
		self.settings = {}

	def configure(self, name, heightmap, texture, posx, posy):
		self.settings["name"] = name
		self.settings["heightmap"] = heightmap
		self.settings["texture"] = texture
		self.settings["x"] = posx
		self.settings["y"] = posy

	def create(self):
		self.test_texture = base.loader.loadTexture(self.settings["texture"])

		self.terrain = GeoMipTerrain(self.settings["name"])
		self.terrain.setHeightfield(self.settings["heightmap"])

		# Set terrain properties
		self.terrain.setBruteforce(False)
		self.terrain.setBlockSize(32)
		self.terrain.setNear(40)
		self.terrain.setFar(100)
		#self.terrain.setMinLevel(16)
		self.terrain.setFocalPoint(base.camera)
		self.terrain.setBorderStitching(True)

		self.terrain.getRoot().setSz(300)
		self.terrain.getRoot().setSx(Globals.TERRAIN_MULT)
		self.terrain.getRoot().setSy(Globals.TERRAIN_MULT)
		self.terrain.getRoot().setPos((self.settings["x"]*512)*Globals.TERRAIN_MULT, \
										  (self.settings["y"]*512)*Globals.TERRAIN_MULT, 0)
		self.terrain.getRoot().setTexture(self.test_texture)
		self.terrain.generate()

	def json_encode(self):
		with open("terrains.json", "a") as write_file:
			json.dump(self.settings, write_file, indent=4)
			write_file.write("\n")

	def json_decode(self, name):
		with open("terrains.json", "r") as read_file:
			terrains = json.load(read_file)
			try:
				self.settings = terrains[name]
			except KeyError:
				print("Key not found in json: "+name)
				return(False)
			else:
				return(True)
