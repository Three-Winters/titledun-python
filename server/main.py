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

c_manager = QueuedConnectionManager()
c_listener = QueuedConnectionListener(c_manager, 0)
c_reader = QueuedConnectionReader(c_manager, 0)
c_writer = ConnectionWriter(c_manager,0)

active_conns=[]

port_address=9099 #No-other TCP/IP services are using this port
backlog=1000 #If we ignore 1,000 connection attempts, something is wrong!

def tskListenerPolling(taskdata):
	if c_listener.newConnectionAvailable():

		rendezvous = PointerToConnection()
		netAddress = NetAddress()
		newConnection = PointerToConnection()

		if cListener.getNewConnection(rendezvous,netAddress,newConnection):
			newConnection = newConnection.p()
			active_conns.append(newConnection) # Remember connection
			c_reader.addConnection(newConnection)     # Begin reading connection
	return Task.cont

def tskReaderPolling(taskdata):
	if c_reader.dataAvailable():
		datagram=NetDatagram()  # catch the incoming data in this instance
		# Check the return value; if we were threaded, someone else could have
		# snagged this data before we did
		if cReader.getData(datagram):
			data_process(datagram)
	return Task.cont

def data_process(datagram):
	print("Processed: "+datagram)

def main():
	tcp_socket = c_manager.openTCPServerRendezvous(port_address,backlog)
	c_listener.addConnection(tcp_socket)

	taskMgr.add(tskListenerPolling,"Poll the connection listener",-39)
	taskMgr.add(tskReaderPolling,"Poll the connection reader",-40)

	while True:
		taskMgr.step()

main()
