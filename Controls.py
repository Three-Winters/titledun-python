import sys
import os

import panda3d.core

import Globals

class Controls():
	def __init__(self):
		self.set_controls()
		base.disable_mouse()
		self.alpha = 0.0
		self.beta = 0.0

	def set_key(self, key, value):
		Globals.key_map[key] = value

	def set_controls(self):
		base.accept("escape", sys.exit)
		base.accept("mouse3", self.set_key, ["mouse3", True])
		base.accept("arrow_left", self.set_key, ["left", True])
		base.accept("arrow_right", self.set_key, ["right", True])
		base.accept("arrow_up", self.set_key, ["forward", True])
		base.accept("arrow_down", self.set_key, ["backward", True])
		base.accept("a", self.set_key, ["cam-left", True])
		base.accept("s", self.set_key, ["cam-right", True])

		base.accept("arrow_left-up", self.set_key, ["left", 2])
		base.accept("arrow_right-up", self.set_key, ["right", False])
		base.accept("arrow_up-up", self.set_key, ["forward", False])
		base.accept("arrow_down-up", self.set_key, ["backward", False])
		base.accept("mouse3-up", self.set_key, ["mouse3", False])
		base.accept("a-up", self.set_key, ["cam-left", False])
		base.accept("s-up", self.set_key, ["cam-right", False])
