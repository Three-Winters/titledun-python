from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionReader
from panda3d.core import ConnectionWriter

class NetworkClient():
	def __init__(self):
		self.timeout = 3000

		self.c_manager = QueuedConnectionManager()
		self.c_reader QueuedConnectionReader(self.c_manager, 0)

	def connect(ip, port):
		connection = c_manager.openTCPClientConection(ip, port, timeout)
		if connection:
			c_reader.addConnection(connection)
			return(True)
		return(False)
