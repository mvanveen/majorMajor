#===============================================================================
# link.py
#===============================================================================
#	Michael Van Veen
#	02/07/10
#==============================================================================
import subprocess
import urllib2
from datetime import datetime

class Link():
	def __init__(self, url, title=""):
		self.__url 					= url
		self.__title 				= title
		self.__referrer 	 	= dict()
		self.__dateCreated	= datetime.now()
		
	def setTitle(self, title):
		self.__title = title

	def getTitle(self):
		return(self.__title)

	def addRefferer(self, url, count):
		self.__referrer[url] = count

	def getURL(self):
		return(self.__url)

	def getReferrers(self):
		return(self.__referrer)

	def getDateCreated(self):
		return(self.__dateCreated)

	def _wget(self):
		'''	Downloads a file with curl, monkeypatches the filename to the 
				object, and returns the filename as a string'''
		self._fileName 	= datetime.isoformat(self.getDateCreated()) + ".out"
		my_args 				= ("curl", "-silent",	self.getURL())

		pipe						=	subprocess.Popen(	my_args, stdout=subprocess.PIPE, 
																			stdin=None, stderr=None, 
																			shell=False) 
		file = open(self._fileName, "wa")

		file.write(str(pipe.communicate()[0]))
		file.close()

		return(self._fileName)
