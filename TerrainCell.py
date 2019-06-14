from panda3d.core import GeoMipTerrain

class TerrainCell:
	def __init__(self, name, heightmap, texture, posx, posy):
		self.test_texture = base.loader.loadTexture(texture)

		self.terrain = GeoMipTerrain(name)
		self.terrain.setHeightfield(heightmap)

		# Set terrain properties
		self.terrain.setBlockSize(32)
		self.terrain.setNear(40)
		self.terrain.setFar(100)
		self.terrain.setFocalPoint(base.camera)
		self.terrain.setBorderStitching(True)

		self.terrain.getRoot().setSz(300)
		self.terrain.getRoot().setSx(8)
		self.terrain.getRoot().setSy(8)
		self.terrain.getRoot().setPos((posx*512)*8, (posy*512)*8, 0)
		self.terrain.getRoot().setTexture(self.test_texture)
		self.terrain.generate()
