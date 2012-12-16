import sys
import sublime, sublime_plugin
from Config import Config
from Controller import Controller
from subprocess import PIPE, Popen,call
import os

class speechCommand(sublime_plugin.TextCommand):


	ctrl = Controller()
	def run(self,edit,toggle):
		print toggle
		#config = configig(self.view)
		#config.run(edit)
		self.edit = edit
		if (toggle == "on"):
			Controller.turnOn(self.view,edit,self)
		else:
			print self.ctrl
			Controller.turnOff()

	def insertText(self,offset,text):
		
		self.view.insert(self.edit,offset,text)
		print 'we got an action!' + text
		#insert the text
		self.edit = self.view.begin_edit()
		pos = self.view.sel()
		pos = pos[0].begin()
		self.view.insert(self.edit, pos, text )

		self.view.sel().clear()
		self.view.sel().add( pos + offset)
		self.view.end_edit(self.edit)


