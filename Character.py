from direct.actor.Actor import Actor

class Character():
	def __init__(self, name):
		self.name = name
		self.cell_x = 0
		self.cell_y = 0

		self.node = base.render.attachNewNode(
			self.name+"_node")


		self.panda_actor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
		self.panda_actor.setScale(0.05, 0.05, 0.05)

		self.node.reparentTo(self.panda_actor)
		self.node.setCompass()
		self.panda_actor.reparentTo(base.render)
		base.camera.reparentTo(self.node)
