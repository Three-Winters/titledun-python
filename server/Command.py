class Command():
	def __init__(self, netobj):
		self.netobj = netobj

		self.commands = {
			"listen": netobj.listen,
			"unlisten": netobj.unlisten
			}

	def execute(self, comm):
		try:
			self.commands[comm]()
		except KeyError:
			print("Not found: "+comm)
