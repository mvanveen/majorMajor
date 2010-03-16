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

from multiprocessing 	import Pool
from BeautifulSoup 		import BeautifulSoup

from link import Link


def normalizeURL(url, fromLink):
# TODO: no trailing "/"'s
	pattern = re.compile("http://")
	if(re.search(pattern, url) == None):
		if not((url[0] == "/") and (fromLink[-1] == "/")):
			url = "/" + url
		return(fromLink + url)
	return(url)

def parse(fileName):
	file 	= open(fileName, 'r').read()
	soup	=	BeautifulSoup(file)

	a = [x for x in soup.findAll('a')]
	
	linkOpen 	= re.compile("<a.*href=\"")
	linkClose	= re.compile("\".*>.*</a>")
	clean 		= lambda x, y: re.subn(x, "", str(y), 1)[0]
	
	return [clean(linkClose, clean(linkOpen, x)) for x in a]

def processLinks(x):
	return(map(lambda y: normalizeURL(y, x.getURL()),
										parse(x._wget())), x)

def makeLink(x):
	return(Link(x))

if __name__ == "__main__":
	p	= Pool(processes=4)
	a = p.map(makeLink, p.map(processLinks, [Link("http://www.google.com")])[0][0])
	print	a
