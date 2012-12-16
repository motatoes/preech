#this file has been generated
#by PREECH config.py for processing
#The input received by sphinx
import sublime,sublime_plugin
import time
try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x


class inputProcessor():
	speechQue = None
	actionQue = None
	def __init__(self,speechQue,actionQue):
		self.speechQue = speechQue
		self.actionQue = actionQue
	def __next_word(self):
		while ( True ):
			word = self.getNextInput() 
			if (word is False):
				time.sleep(1)
			else:
				break
		return word
	def getNextInput(self):
		try:  line = self.speechQue.get_nowait()
		except Empty:
		    return False
		else: # got line
		    return line
	def getSym(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='continue'):
			pass
		else:
			self.getSym()


	def moreArgs(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='continue'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
		elif (value =='next'):
			act = action()
			act.setInsert(',')
#			self.view.insert(edit, pos, ',' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			act.setOffset(0)
			self.getSym()
			#alright we need to wait for her to enter a symbol name 
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			act.setOffset(0)
			self.moreArgs()
		else:
			self.moreArgs()


	def start(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='function'):
			act = action()
			act.setInsert('def ():')
#			self.view.insert(edit, pos, 'def ():' )
			act.setOffset(4)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			act.setOffset(0)
			self.getSym()
			#alright we need to wait for her to enter a symbol name 
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			act.setOffset(0)
			self.fnargs()
			act.setOffset(-12)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			act.setOffset(0)
			self.fnbody()
		else:
			self.start()


	def fnargs(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='continue'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
		elif (value =='next'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			act.setOffset(0)
			self.getSym()
			#alright we need to wait for her to enter a symbol name 
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			act.setOffset(0)
			self.moreArgs()
		else:
			self.fnargs()


	def fnbody(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='continue'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
		else:
			self.fnbody()


#specifies what text to insert and then where to move
class action():
	def __init__(self):
		pass
	def setInsert(self,toinsert):
		self.toinsert = toinsert
	def setOffset(self,offset):
		self.offset = offset
