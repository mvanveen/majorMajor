#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ==============================================================================
# hostName.py
# ==============================================================================
# Author: 				Michael Van Veen
# Created: 				03-23-2010
# Last Modified:	2010-03-23T05:25:01-0700
# ==============================================================================
#	The duty of this file is to parse a given set of url's and output a list 
# of url's.
# 
# Suggested tab width: 2
# ==============================================================================

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


if __name__ == "__main__":
	file 			= [Link(x[:-1]) for x in open("input", "r").readlines()]
	output 		= open("input", "a")
	processed = [y[0] for y in [processLinks(z) for z in file]]

	print processed
	[output.writelines(["".join((x, '\n')) for x in processed])]
