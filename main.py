from math import pi, sin, cos

import sys
import os

#import direct.directbase.DirectStart
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from panda3d.core import TextNode
from panda3d.core import Point3
import panda3d.core


import Globals
from Controls import Controls

class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		props = panda3d.core.WindowProperties()
		props.set_title("Demo")
		self.win.request_properties(props)
		self.win.set_clear_color((0, 0, 0, 1))

		Globals.game_states.request("MainMenu")

		taskMgr.add(self.move, "moveTask")
		Globals.g_task_manager = taskMgr
		self.cons = Controls()

	def move(self, task):

		#dt is the time since last frame
		dt = globalClock.get_dt()

		if Globals.key_map["left"]:
			self.camera.setX(self.camera.getX() - 5.0)
		if Globals.key_map["right"]:
			self.camera.setX(self.camera.getX() + 5.0)
		if Globals.key_map["forward"]:
			self.camera.setZ(self.camera.getZ() + 5.0)
		if Globals.key_map["backward"]:
			self.camera.setZ(self.camera.getZ() - 5.0)
		if Globals.key_map["mouse3"]:
			c_x_pos = self.win.getPointer(0).getX()
			c_y_pos = self.win.getPointer(0).getY()
			c_x_pos -= self.r_x_pos
			c_y_pos -= self.r_y_pos
			self.cons.alpha -= c_x_pos * 0.05
			self.cons.beta -= c_y_pos * 0.05
			self.camera.setHpr(self.cons.alpha, self.cons.beta, 0.0)
			self.win.movePointer(0, int(self.r_x_pos), int(self.r_y_pos))
		if not Globals.key_map["mouse3"]:
			self.r_x_pos = self.win.getPointer(0).getX()
			self.r_y_pos = self.win.getPointer(0).getY()
		return task.cont

app = MyApp()
app.run()
