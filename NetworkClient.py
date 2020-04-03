from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionReader
from panda3d.core import ConnectionWriter
from panda3d.core import ConnectionManager

from direct.distributed.PyDatagram import PyDatagram

class NetworkClient():
	def __init__(self):
		self.timeout = 3000

		self.c_manager = QueuedConnectionManager()
		self.c_reader = QueuedConnectionReader(self.c_manager, 0)
		self.c_writer = ConnectionWriter(self.c_manager,0)

	def connect(self, ip, port):
		self.connection = self.c_manager.openTCPClientConnection(ip, port, self.timeout)
		if self.connection:
			self.c_reader.addConnection(self.connection)
			return(True)
		return(False)

	def disconnect(self):
		if self.connection:
			self.c_manager.closeConnection(self.connection)
		else:
			print("Trying to disconnect while not connected!")

	def send_data(self):
		data = PyDatagram()
		data.addString("Hello, world!")
		self.c_writer.send(data, self.connection)
