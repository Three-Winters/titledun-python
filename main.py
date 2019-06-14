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

class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		props = panda3d.core.WindowProperties()
		props.set_title("Demo")
		self.win.request_properties(props)
		self.win.set_clear_color((0, 0, 0, 1))

		Globals.game_states.request("MainMenu")

		self.key_map = {
			"left": 0, "right": 0, "forward": 0, "backward": 0,"cam-left": 0, "cam-right": 0, "mouse3":0}

		self.set_controls()

		taskMgr.add(self.move, "moveTask")
		Globals.g_task_manager = taskMgr

		# Disable the camera trackball controls.
		self.disable_mouse()
		Globals.g_render = self.render
		self.alpha = 0.0
		self.beta = 0.0

	def set_key(self, key, value):
		self.key_map[key] = value

	def set_controls(self):
		self.accept("escape", sys.exit)
		self.accept("mouse3", self.set_key, ["mouse3", True])
		self.accept("arrow_left", self.set_key, ["left", True])
		self.accept("arrow_right", self.set_key, ["right", True])
		self.accept("arrow_up", self.set_key, ["forward", True])
		self.accept("arrow_down", self.set_key, ["backward", True])
		self.accept("a", self.set_key, ["cam-left", True])
		self.accept("s", self.set_key, ["cam-right", True])

		self.accept("arrow_left-up", self.set_key, ["left", False])
		self.accept("arrow_right-up", self.set_key, ["right", False])
		self.accept("arrow_up-up", self.set_key, ["forward", False])
		self.accept("arrow_down-up", self.set_key, ["backward", False])
		self.accept("mouse3-up", self.set_key, ["mouse3", False])
		self.accept("a-up", self.set_key, ["cam-left", False])
		self.accept("s-up", self.set_key, ["cam-right", False])

	def move(self, task):

		#dt is the time since last frame
		dt = globalClock.get_dt()

		if self.key_map["left"]:
			self.camera.setX(self.camera.getX() - 1.0)
		if self.key_map["right"]:
			self.camera.setX(self.camera.getX() + 1.0)
		if self.key_map["forward"]:
			self.camera.setZ(self.camera.getZ() + 1.0)
		if self.key_map["backward"]:
			self.camera.setZ(self.camera.getZ() - 1.0)
		if self.key_map["mouse3"]:
			c_x_pos = self.win.getPointer(0).getX()
			c_y_pos = self.win.getPointer(0).getY()
			c_x_pos -= self.r_x_pos
			c_y_pos -= self.r_y_pos
			self.alpha -= c_x_pos * 0.05
			self.beta -= c_y_pos * 0.05
			self.camera.setHpr(self.alpha, self.beta, 0.0)
			self.win.movePointer(0, int(self.r_x_pos), int(self.r_y_pos))
		if not self.key_map["mouse3"]:
			self.r_x_pos = self.win.getPointer(0).getX()
			self.r_y_pos = self.win.getPointer(0).getY()
		return task.cont

app = MyApp()
app.run()
