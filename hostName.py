# hostName.py
from datetime import datetime
from Link import Link

# Important bits:
# - Specify hostname
#	- Prune according to global rules (more on this bit later)
#	-- and robots.txt file
# - Guarantee timeout

class Hostname():
	def __init__(self, hostname):
		self.__hostname 			= str(hostname)
		self.__links					= dict() #SQLite Object?
		self.__lastCheckTime
	# And now for some prototypes
	Hostname.pop() 					# Returns a link to check
	Hostname.setScheduler() # Sets the criterum to scheduler
