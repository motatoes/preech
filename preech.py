import sys
import sublime, sublime_plugin

from subprocess import PIPE, Popen,call
import threading
try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x


class PreechCommand(sublime_plugin.TextCommand):
	q = Queue()
	rec = None
	#get the next uttered line
	def get_next_line(self):
		try:  line = self.q.get_nowait() # or q.get(timeout=.1)
		except Empty:
		    #print('no output yet')
		    return False
		else: # got line
		    # ... do something with line
		    return line + '###'

	def process_next_line(self):
		line = self.get_next_line()
		if (line):
			##do some processing with the line here 
			print line
			pass
		
		if self.rec.is_alive():
			#repeat if the thread is still alive
			sublime.set_timeout(lambda: self.process_next_line(), 100)  

	    
	def run(self, edit):
	

		# read line without blocking
		self.rec = RecognizerThread(self.q)
		self.rec.setDaemon(True)
		self.rec.start()

		sublime.set_timeout(lambda: self.process_next_line(), 100)  



		#self.check_output()
		# ... do other things here

class RecognizerThread(threading.Thread):  
    def __init__(self, queue,):  
		ON_POSIX = 'posix' in sys.builtin_module_names
		
		p = Popen(['java','-jar','sphinx/jython_standalone.jar','sphinx/init.py'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
		#self.t = Thread(target=enqueue_output, args=())
		self.queue = queue

		self.out = p.stdout 
		self.result = None  
		threading.Thread.__init__(self)
    def run(self):  
	    for line in iter(self.out.readline, b''):
	    	print 'now reading line'
	        self.queue.put(line)
	    self.out.close()