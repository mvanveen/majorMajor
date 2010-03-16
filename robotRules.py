#===============================================================================
# robotRules.py
#===============================================================================
#	Michael Van Veen
#	02/24/10
#==============================================================================
# This file describes a robotRules class which can be used to clear a 
# hostname's internal links of illegal urls.  This is in order to comply with
# our politeness guarantee

import urllib2

class robotRules():
	def __init__(self, hostname):
		self.__acquireRobotsTxt(hostname)
		
	# Grabs robots.txt file
	def __acquireRobotsTxt(hostname):
		#TODO: 	Draft requirements for url cleaning, 
		#TODO		and ensure that they are consistent
		robotsUrl = hostname + "/robots.txt"
		
