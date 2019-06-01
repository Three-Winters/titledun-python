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
			"left": 0, "right": 0, "forward": 0, "cam-left": 0, "cam-right": 0}

		self.set_controls()

		taskMgr.add(self.move, "moveTask")

		# Disable the camera trackball controls.
		self.disable_mouse()

	def set_key(self, key, value):
		self.key_map[key] = value

	def set_controls(self):
		self.accept("escape", sys.exit)
		self.accept("arrow_left", self.set_key, ["left", True])
		self.accept("arrow_right", self.set_key, ["right", True])
		self.accept("arrow_up", self.set_key, ["forward", True])
		self.accept("a", self.set_key, ["cam-left", True])
		self.accept("s", self.set_key, ["cam-right", True])

		self.accept("arrow_left-up", self.set_key, ["left", False])
		self.accept("arrow_right-up", self.set_key, ["right", False])
		self.accept("arrow_up-up", self.set_key, ["forward", False])
		self.accept("a-up", self.set_key, ["cam-left", False])
		self.accept("s-up", self.set_key, ["cam-right", False])

	def move(self, task):

		#dt is the time since last frame
		dt = globalClock.get_dt()

		if self.key_map["left"]:
			print("Left pressed")
		if self.key_map["right"]:
			print("Right pressed")
		if self.key_map["forward"]:
			print("forward pressed")

		return task.cont

app = MyApp()
app.run()
