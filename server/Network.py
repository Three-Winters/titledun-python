from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionListener
from panda3d.core import QueuedConnectionReader
from panda3d.core import ConnectionWriter

from panda3d.core import PointerToConnection
from panda3d.core import NetAddress

from panda3d.core import NetDatagram
import direct.task
from direct.showbase.ShowBase import taskMgr
from direct.task.Task import Task

from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

class Network():
	def __init__(self):
		self.c_manager = QueuedConnectionManager()
		self.c_listener = QueuedConnectionListener(self.c_manager, 0)
		self.c_reader = QueuedConnectionReader(self.c_manager, 0)
		self.c_writer = ConnectionWriter(self.c_manager,0)

		self.active_conns=[]

		self.port_address=9099 #No-other TCP/IP services are using this port
		self.backlog=1000 #If we ignore 1,000 connection attempts, something is wrong!

		#tcp_socket = c_manager.openTCPServerRendezvous(port_address,backlog)
		#self.tcp_socket = self.c_manager.openTCPServerRendezvous("0.0.0.0", 9099, 1000)
		#self.c_listener.addConnection(self.tcp_socket)

	def tsk_listener_pol(self, taskdata):
		if self.c_listener.newConnectionAvailable():

			rendezvous = PointerToConnection()
			netAddress = NetAddress()
			newConnection = PointerToConnection()

			if self.c_listener.getNewConnection(rendezvous,netAddress,newConnection):
				print("Connected: "+str(netAddress))
				newConnection = newConnection.p()
				self.active_conns.append(newConnection) # Remember connection
				self.c_reader.addConnection(newConnection)     # Begin reading connection
		return Task.cont

	def tsk_reader_pol(self, taskdata):
		if self.c_reader.dataAvailable():
			datagram=NetDatagram()  # catch the incoming data in this instance
			# Check the return value; if we were threaded, someone else could have
			# snagged this data before we did
			if self.c_reader.getData(datagram):
				self.data_process(datagram)
		return Task.cont

	def data_process(self, datagram):
			it = PyDatagramIterator(datagram)
			message = it.getString()
			print("Processed: "+message+" from: "+str(datagram.getAddress()))

	def listen(self):
		print("Now listening on all addresses on port 9099")
		self.tcp_socket = self.c_manager.openTCPServerRendezvous("0.0.0.0", 9099, 1000)
		self.c_listener.addConnection(self.tcp_socket)
		taskMgr.add(self.tsk_listener_pol, "Poll connection listener", -39)
		taskMgr.add(self.tsk_reader_pol, "Pol the connection reader", -40)

	def unlisten(self):
		print("Stopping listen")
		self.c_listener.closeConnection(self.tcp_socket)
