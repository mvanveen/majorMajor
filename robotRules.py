# ==============================================================================
# robotRules.py
# ==============================================================================
# Author: 				Michael Van Veen
# Created: 				03-23-2010
# Last Modified:	2010-03-23T00:33:18-0700
# ==============================================================================
# DESCRIPTION
# ==============================================================================

import urllib2

class robotRules():
	def __init__(self, hostname):
		self.__acquireRobotsTxt(hostname)
		
	# Grabs robots.txt file
	def __acquireRobotsTxt(hostname):
		#TODO: 	Draft requirements for url cleaning, 
		#TODO		and ensure that they are consistent
		robotsUrl = hostname + "/robots.txt"
		
