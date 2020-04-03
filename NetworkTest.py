import Globals
from NetworkClient import NetworkClient

class NetworkTest():
	def __init__(self):
		self.n = NetworkClient()
		self.n.connect("127.0.0.1", 9099)
		self.n.send_data()
		#self.n.disconnect()

	def request_state(self, name):
		Globals.game_states.request(name)
