import sys,os
import sublime,sublime_plugin
from subprocess import PIPE, Popen,call
import threading
from inputProcessor  import inputProcessor
import time
from speech import speechCommand

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x



class RecognizerThread(threading.Thread): 
	p=None

	def __init__(self, queue):  
		print 'initializing speech ....'
		#self.t = Thread(target=enqueue_output, args=())
		self.queue = queue
		threading.Thread.__init__(self)
	def killRecognizer(self):
		print self.p
		self.p.terminate()
	def run(self):
		print 'hello from the run'	
		ON_POSIX = 'posix' in sys.builtin_module_names
		dir = sublime.packages_path()
		sphinxdir =  os.path.join(dir, 'preech\sphinx')
		jfn  = os.path.join(sphinxdir, 'jython_standalone.jar')
		initfn  = os.path.join(sphinxdir, 'init.py')
		self.p = Popen(['java','-jar',jfn,initfn,sphinxdir], shell=False,stdout=PIPE,stderr=PIPE,bufsize=1, close_fds=ON_POSIX)
		self.out = self.p.stdout 
		for line in iter(self.out.readline, b''):
			print 'now reading line'	
			print line.rstrip('\n')
			self.queue.put(line.rstrip('\r\n'))
		
		self.out.close()



class ProcessorThread(threading.Thread):  
    def __init__(self, speechqueue, actionqueue):
    	self.speechqueue = speechqueue
    	self.actionqueue = actionqueue
    	self.p = inputProcessor(self.speechqueue, self.actionqueue)
    	threading.Thread.__init__(self)
    def run(self):
    	self.p.start()

class processorMain():
	def __init__(self,actionQue):
		self.actionQue = actionQue
	def begin(self):
		sublime.set_timeout(self.insertText,1000)
	def setView(self,view):
		self.view = view
	def setSpeechMain(self,sm):
		self.speechMain = sm
	def setEdit(self,edit):
		self.edit = edit
    
	def insertText(self):

		try:  action = self.actionQue.get_nowait()
		except Empty:
		    pass
		else: # got action obj
			self.speechMain.insertText(action.offset, action.toinsert)
		#rinse and repeat ...
		sublime.set_timeout(self.insertText,1000)

	
class Controller():

	#this is the queue that receives recognizer text
	speechQueue = Queue()
	#this is the que that receives action states for manip. that file
	actionQueue = Queue()
	rec = RecognizerThread(speechQueue)
	processor = ProcessorThread(speechQueue,actionQueue)
	pmain = processorMain(actionQueue)
#inadequate, i know
	@classmethod
	def turnOn(self,view,edit,speechMain):
		#Start the recognizer
		self.rec.setDaemon(True)
		self.rec.start()

		self.processor.setDaemon(True)
		self.processor.start()
		 
		self.pmain.setSpeechMain(speechMain)
		self.pmain.begin()
	
	@classmethod
	def turnOff(self):
		self.rec.killRecognizer()
		pass



