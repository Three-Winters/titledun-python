from panda3d.core import GeoMipTerrain
from panda3d.core import CollisionCapsule
from panda3d.core import CollisionNode
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerEvent
from direct.showbase.DirectObject import DirectObject

#ODE
from panda3d.ode import OdeSimpleSpace, OdeJointGroup
from panda3d.ode import OdeBoxGeom, OdePlaneGeom
from panda3d.ode import OdeBody, OdeMass, OdeWorld, OdeTriMeshData, OdeTriMeshGeom, OdeSpace

import Globals

import json

class TerrainCell(DirectObject):
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

		#self.fast_cols(16, 16)
		#self.generate_collisions()
		#self.ode_cols()

	def ode_cols(self):
		world = OdeWorld()
		world.setGravity(0,0,-9)
		world.initSurfaceTable(1)
		world.setSurfaceEntry(0, 0, 150, 0.0, 9.1, 0.9, 0.00001, 0.0, 0.002)

		# Create a space and add a contactgroup to it to add the contact joints
		space = OdeSimpleSpace()
		space.setAutoCollideWorld(world)
		contactgroup = OdeJointGroup()
		space.setAutoCollideJointGroup(contactgroup)
		space.autoCollide()

		#try ODE for collisions
		t_trimesh = OdeTriMeshData(self.terrain.getRoot(), True)
		t_geom = OdeTriMeshGeom(space, t_trimesh)

	def fast_cols(self, x, y):
		#simpler, and faster
		return(self.terrain.getElevation(x, y), self.terrain.getNormal(x, y))

	def generate_collisions(self):
		#try panda's collisions
		print("generating collisions...")
		x = 512
		y = 512
		while x:
			z = self.terrain.getElevation(x, y)
			cap = CollisionCapsule(0, 0, 1, 1)
			self.collision_node = base.render.attachNewNode(CollisionNode('cap1'))
			self.collision_node.node().addSolid(cap)
			#self.collision_node.show()
			#self.accept('into-cap1', self.hanev)
			#self.accept('out-cap1', self.hanev)
			self.collision_node.setPos(x, y, z*300)
			x -= 16
			y = 512
			while y:
				z = self.terrain.getElevation(x, y)
				cap = CollisionCapsule(0, 0, 0, 0, 0, 1, 1)
				self.collision_node = base.render.attachNewNode(CollisionNode('cap1'))
				self.collision_node.node().addSolid(cap)
				self.collision_node.show()
				#self.accept('into-cap1', self.hanev)
				#self.accept('out-cap1', self.hanev)
				self.collision_node.setPos(x, y, z*300)
				y -= 16

		base.cTrav.addCollider(self.collision_node, base.mchandler)

		self.collision_node.setPos(10, 0, -3)

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

	def bam_encode(self):
		self.terrain.getRoot().writeBamFile(self.settings["name"])
