#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#===============================================================================
# link.py
#===============================================================================
#	Michael Van Veen
#	02/07/10
#==============================================================================
import subprocess
import urllib2
from datetime import datetime
import codecs
import magic
#TODO: Change from subprocess call to urllib2
#TODO: Change user-agent to "majorMajor"

class Link():
	def __init__(self, url):
		self.__url 					= str(url)
		self.__referrer 	 	= dict()
		self.__dateCreated	= datetime.now()
		self.__dateModified	= datetime.now()
		self.__contentType	= None
		self.__Content			= list()

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

		self.__Content.append(datetime.isoformat(self.getDateCreated()) + ".out")

		self.__fileName = self.__Content[len(self.__Content)-1]
		#my_args 				= ("curl", "-silent",	"-A Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/9.10 (karmic) Firefox/3.5.3", self.getURL())

		my_args					= ("wget", "-qO-", self.getURL())
		pipe						=	subprocess.Popen(	my_args, stdout=subprocess.PIPE, 
																			stdin=None, stderr=None, 
																			shell=False) 
		file 	= codecs.open(self.__fileName, "wa", 'utf-8')
		out 	= pipe.communicate()[0].decode('utf-8', "replace")
		file.write(out)
		file.close()
		#libMagic 						= magic.open(magic.MAGIC_NONE)
		#self.__contentType 	= libMagic.file(out.decode("ascii", "ignore"))

		return(self.__Content[len(self.__Content)-1].decode("utf-8", "replace"))

