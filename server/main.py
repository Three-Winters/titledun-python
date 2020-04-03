from direct.showbase.ShowBase import taskMgr
from direct.task.Task import Task

from ConsoleInput import ConsoleInput
from Network import Network

def main():
	network = Network()
	console = ConsoleInput(network)
	network.listen()

	while True:
		taskMgr.step()

main()
