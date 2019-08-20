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

		Globals.g_task_manager = taskMgr
		#Globals.win = self.win
		Globals.controls = Controls()

app = MyApp()
app.run()
