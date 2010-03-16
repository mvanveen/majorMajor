#===============================================================================
# hostName.py
#===============================================================================
#	Michael Van Veen
#	02/22/10
#==============================================================================
import md5
import sqlite3

from datetime import datetime
from Link import Link

#TODO Use a huffman code to encode urls

class Hostname():
	def __init__(self, hostname):
		self.__hostname 			= str(hostname)
		self.__linkDB					= md5.new(self.__hostname).digest() + ".db"

		#	List of regeXPS accrued from robots.txt
		self._robotRules 			= self.__acquireRobotRules()	

		self.__lastCheckTime	= datetime.now()
		self.__offSetTime			= datetime.now()
		self._tableCreated		= False

	
	# Returns a link to check.  Updates clock.
	# TODO: Determine correct timings to send and keep
	def pop(self):
		self.__lastCheckTime 	= datetime.now()
		self.__offSetTime 		= datetime.now()
		return(self.getURL(), self.__lastCheckTime)

	# TODO: Implement
	# Creates a SQLiteDB when none has been instanced
	def __createDB(self):
		
	# TODO: Implement
	# Grabs robots.txt file and develops rules to prune state space
	def __acquireRobotRules(self):
	
	# Checks to see if a table has been created.  If not, it constructs one.
	def __tableCheck(self)
		if not(self.__tableCreated):
			self.__createDB()
			self.__tableCreated = true

	#TODO: implement
	# inserts a local URL into a sqlite table
	def insertLocalURL(self):
		self.__tableCheck()

	#TODO: implement
	def insertExternURL(self):
		self.__tableCheck()
	
	#TODO: Implement
	#Used to set an arbitrary scheduling function for the host name
	def setScheduler(self):

