class State():
	def __init__(self, fun, name):
		self.name = name
		self.fun = fun

	def enter(self):
		print(name+" entered.")
		self.obj = self.fun()

	def exit(self):
		print(name+" exited")
		del self.obj
