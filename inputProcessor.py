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


	def fname(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='add'):
			act = action()
			act.setInsert('add')
#			self.view.insert(edit, pos, 'add' )
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='constructuor'):
			act = action()
			act.setInsert('__init__')
#			self.view.insert(edit, pos, '__init__' )
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.fname()


	def classname(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='arithmetic'):
			act = action()
			act.setInsert('Arithmetic')
#			self.view.insert(edit, pos, 'Arithmetic' )
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.classname()


	def start(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='class'):
			act = action()
			act.setInsert('class ():\n')
#			self.view.insert(edit, pos, 'class ():\n' )
			act.setOffset(6)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.classname()
			act.setOffset(5)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.classbody()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='function'):
			act = action()
			act.setInsert('def ():\n')
#			self.view.insert(edit, pos, 'def ():\n' )
			act.setOffset(4)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.fname()
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.fnargs()
			act.setOffset(4)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.fnbody()
			act.setOffset(0)
			self.actionQue.put(act)
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
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='next'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			#alright we need to wait for her to enter a symbol name 
			self.getSym()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.moreArgs()
			act.setOffset(0)
			self.actionQue.put(act)
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
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.fnbody()


	def moreArgs(self):
		value = self.__next_word()
		if (False):
			pass
		elif (value =='continue'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='next'):
			act = action()
			act.setInsert(',')
#			self.view.insert(edit, pos, ',' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			#alright we need to wait for her to enter a symbol name 
			self.getSym()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.moreArgs()
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.moreArgs()


#specifies what text to insert and then where to move
class action():
	def __init__(self):
		pass
	def setInsert(self,toinsert):
		self.toinsert = toinsert
	def setOffset(self,offset):
		self.offset = offset
