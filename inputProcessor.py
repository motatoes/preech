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
	def acceptDefaultStates(self,value):
		if (False):
			pass
		elif (value == 'indent' ):
			act = action()
			act.setInsert('    ')
			act.setOffset(0)
			self.actionQue.put(act)
			return True
		elif (value == 'new line' ):
			act = action()
			act.setInsert('\n')
			act.setOffset(0)
			self.actionQue.put(act)
			return True
		return False


	def boolexp(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.boolexp()
		if (False):
			pass
		elif (value =='double equals'):
			act = action()
			act.setInsert('  == ')
#			self.view.insert(edit, pos, '  == ' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(4)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='greater than'):
			act = action()
			act.setInsert('  > ')
#			self.view.insert(edit, pos, '  > ' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='less than'):
			act = action()
			act.setInsert('  < ')
#			self.view.insert(edit, pos, '  < ' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='greater than or equals'):
			act = action()
			act.setInsert('  >= ')
#			self.view.insert(edit, pos, '  >= ' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(4)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='less than or equals'):
			act = action()
			act.setInsert('  <= ')
#			self.view.insert(edit, pos, '  <= ' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(4)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='not equals'):
			act = action()
			act.setInsert('  <> ')
#			self.view.insert(edit, pos, '  <> ' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(4)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.boolexp()


	def ifbody(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.ifbody()
		if (False):
			pass
		elif (value =='assignment'):
			act = action()
			act.setInsert('  = \n')
#			self.view.insert(edit, pos, '  = \n' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expression()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='pass'):
			act = action()
			act.setInsert('pass')
#			self.view.insert(edit, pos, 'pass' )
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.ifbody()


	def fnbody(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.fnbody()
		if (False):
			pass
		elif (value =='assignment'):
			act = action()
			act.setInsert('  = \n')
#			self.view.insert(edit, pos, '  = \n' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expression()
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.fnbody()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='if'):
			act = action()
			act.setInsert(' if ():\n\n')
#			self.view.insert(edit, pos, ' if ():\n\n' )
			act.setOffset(5)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.boolexp()
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.ifbody()
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.elseClause()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='return'):
			act = action()
			act.setInsert('return ')
#			self.view.insert(edit, pos, 'return ' )
			act.setOffset(7)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expression()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='continue'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.fnbody()


	def elseClause(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.elseClause()
		if (False):
			pass
		elif (value =='else if'):
			act = action()
			act.setInsert('elif ():\n\n')
#			self.view.insert(edit, pos, 'elif ():\n\n' )
			act.setOffset(6)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.boolexp()
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.ifbody()
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.elseClause()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='else clause'):
			act = action()
			act.setInsert('else:\n')
#			self.view.insert(edit, pos, 'else:\n' )
			act.setOffset(6)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.ifbody()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='continue'):
			act = action()
			act.setInsert('')
#			self.view.insert(edit, pos, '' )
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.elseClause()


	def classname(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.classname()
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
		if(self.acceptDefaultStates(value)):
			self.start()
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
			act.setOffset(4)
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
			act.setOffset(3)
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
		if(self.acceptDefaultStates(value)):
			self.fnargs()
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
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.moreArgs()
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.fnargs()


	def fname(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.fname()
		if (False):
			pass
		elif (value =='add'):
			act = action()
			act.setInsert('add')
#			self.view.insert(edit, pos, 'add' )
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='multiply'):
			act = action()
			act.setInsert('multiply')
#			self.view.insert(edit, pos, 'multiply' )
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='divide'):
			act = action()
			act.setInsert('divide')
#			self.view.insert(edit, pos, 'divide' )
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='maximum'):
			act = action()
			act.setInsert('max')
#			self.view.insert(edit, pos, 'max' )
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


	def var(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.var()
		if (False):
			pass
		elif (value =='variable one'):
			act = action()
			act.setInsert('var1')
#			self.view.insert(edit, pos, 'var1' )
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='variable two'):
			act = action()
			act.setInsert('var2')
#			self.view.insert(edit, pos, 'var2' )
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='result'):
			act = action()
			act.setInsert('result')
#			self.view.insert(edit, pos, 'result' )
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.var()


	def moreArgs(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.moreArgs()
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
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.moreArgs()
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.moreArgs()


	def expressionTerm(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.expressionTerm()
		if (False):
			pass
		elif (value =='plus'):
			act = action()
			act.setInsert(' + ')
#			self.view.insert(edit, pos, ' + ' )
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expressionTerm()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='minus'):
			act = action()
			act.setInsert(' - ')
#			self.view.insert(edit, pos, ' - ' )
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expressionTerm()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='divided by'):
			act = action()
			act.setInsert(' / ')
#			self.view.insert(edit, pos, ' / ' )
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expressionTerm()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='times'):
			act = action()
			act.setInsert(' * ')
#			self.view.insert(edit, pos, ' * ' )
			act.setOffset(3)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expressionTerm()
			act.setOffset(0)
			self.actionQue.put(act)
		elif (value =='continue'):
			act = action()
			act.setInsert('\n')
#			self.view.insert(edit, pos, '\n' )
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.expressionTerm()


	def expression(self):
		value = self.__next_word()
		if(self.acceptDefaultStates(value)):
			self.expression()
		if (False):
			pass
		elif (value =='expression'):
			act = action()
			act.setInsert(' ')
#			self.view.insert(edit, pos, ' ' )
			act.setOffset(1)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.var()
			act.setOffset(0)
			self.actionQue.put(act)
			act = action()
			act.setInsert('')
			self.expressionTerm()
			act.setOffset(0)
			self.actionQue.put(act)
		else:
			self.expression()


#specifies what text to insert and then where to move
class action():
	def __init__(self):
		pass
	def setInsert(self,toinsert):
		self.toinsert = toinsert
	def setOffset(self,offset):
		self.offset = offset
