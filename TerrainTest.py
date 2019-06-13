import Globals
from TerrainManager import TerrainManager

class TerrainTest():
	def __init__(self):
		print("TerrainTest object created")
		self.tm = TerrainManager(Globals.g_render)
