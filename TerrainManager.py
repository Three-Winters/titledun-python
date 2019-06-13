from panda3d.core import GeoMipTerrain

class TerrainManager:
	def __init__(self, render):
		#intialise terrain list to zeroes!
		self.terrain_list = [[0 for x in range(16)] for y in range(16)]

		self.terrain = GeoMipTerrain("simple terrain")
		self.terrain.setHeightfield("field.png")
		self.terrain.getRoot().reparentTo(render)
		self.terrain.getRoot().setSz(100)
		self.terrain.generate()
