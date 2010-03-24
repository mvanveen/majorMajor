# ==============================================================================
# file.py
# ==============================================================================
# Author: 				Michael Van Veen
# Created: 				03-22-2010
# Last Modified:	2010-03-23T05:27:35-0700
# ==============================================================================
# Describes file objects.
# ==============================================================================
import re

class File():
	def __init__(self, origFileName):
		pattern = re.compile('\.')
		self.__extension 			= str(re.split(pattern, origFileName)[-1])
		self.__origFileName		= str(origFileName)
		self.__fileName				= str(fileName)

		def __isBinary(self):
		binaryTypes =	 {	"flac":True,
											"mp3":True,
											"ogg":True,
											"mp4":True,
											"mp3":True,
											"txt":False,
											"html":False
										} 
		try:
			return(binaryTypes[self.__extension])
		except KeyError:
			# TODO: Log binary type error
			return(True)

	def getFileName(self):
		return(self.__fileName)

	def getFileHandler(self, mode):
		if (self.__isBinary):
			mode += 'b'
		return(open(self.__fileName, mode))

