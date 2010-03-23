#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#===============================================================================
# majorMajor.py
#===============================================================================
#	Michael Van Veen
#	01/31/10
#==============================================================================
#	The duty of this file is to parse a given set of url's and output a list 
# of url's.

import pprint
import sys
import re
import codecs

from multiprocessing 	import Pool
from BeautifulSoup 		import BeautifulSoup

from link import Link

def normalizeURL(url, fromLink):
# TODO: no trailing "/"'s
	url 			= str(url).decode("ascii", "replace")
	fromLink	= str(fromLink).decode("ascii", "replace")
	charTable = {105: True, 102:True, 98:True,95:True, 84:True, 83:True, 82:True}
							
	pattern = re.compile("http://")
	if(re.search(pattern, url) == None):
		#match = lambda x: charTable.has_key(ord(url[0]))
		match = lambda x: ord(x) == 62
		if match(url[0]) and match(fromLink[-1]):
			url = u"/" + url
		return(fromLink + url)
	return(url)

def parse(fileName):
	fileName.encode("utf8")
	file 	= codecs.open(fileName, 'r', 'utf-8').read()
	soup	=	BeautifulSoup(file)

	a = [str(x) for x in soup.findAll('a')]

	linkOpen 	= re.compile("<a.*href=\"")
	linkClose	= re.compile("\".*>.*</a>")
	clean 		= lambda x, y: re.subn(x, '', y, 1)[0]
	return([clean(linkClose, clean(linkOpen, x)) for x in a])

def processLinks(x):
	return(map(lambda y: normalizeURL(y, x.getURL()),
										parse(x._wget())), x)

def makeLink(x):
	return(Link(x))

if __name__ == "__main__":
	#p			= Pool(processes=4)
	input = sys.argv[1]
	#a = p.map(makeLink, p.map(processLinks, [Link("http://www.google.com")])[0][0])
	#a = p.map(makeLink, p.map(processLinks, [Link(input)[0][0])
	file = open("input", "r").readlines()
	file = [Link(x) for x in file]
	pprint.pprint(map(processLinks, file)[0][0])
	#print	map(lambda x: processLinks(x), [Link(input)])
