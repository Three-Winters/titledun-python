import Globals
from NetworkClient import NetworkClient

class NetworkTest():
	def __init__(self):
		self.n = NetworkClient()
		if self.n.connect("127.0.0.1", 9099) == True:
			print("Connected to server.")
			self.n.send_data()
		else:
			print("Failed to connect to server")
		#self.n.disconnect()

	def request_state(self, name):
		Globals.game_states.request(name)
