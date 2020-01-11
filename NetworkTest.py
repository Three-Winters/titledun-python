import Globals
from NetworkClient import NetworkClient

class NetworkTest():
	def __init__(self):
		self.n = NetworkClient()
		self.n.connect("127.0.0.1", 9099)

	def request_state(self, name):
		Globals.game_states.request(name)
