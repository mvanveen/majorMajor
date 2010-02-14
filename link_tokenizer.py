#===============================================================================
# link_tokenizer.py
#===============================================================================
#	Michael Van Veen
#	01/31/10
#==============================================================================
#	The duty of this file is to parse a given set of url's and output a list 
# of url's.
#
import pprint
import sys
import re
#from multiprocessing 	import Pool
from BeautifulSoup 		import BeautifulSoup
from link import Link

def parse(fileName):
	file 	= open(fileName, 'r').read()
	soup	=	BeautifulSoup(file)

	a = [x for x in soup.findAll('a')]
	
	linkOpen 	= re.compile("<a.*href=\"")
	linkClose	= re.compile("\".*>.*</a>")
	clean 		= lambda x, y: re.subn(x, "", str(y), 1)[0]
	
	return [clean(linkClose, clean(linkOpen, x)) for x in a]

def normalizeURL(url, fromLink):
# TODO: no trailing "/"'s
#				
	pattern = re.compile("http://")
	if(re.search(pattern, url) == None):
		if not((url[0] == "/") and (fromLink[-1] == "/")):
			url = "/" + url
		return(fromLink + url)
	return(url)

def prune(x):
# Make sure url's are allowed
	return(x)

#input = sys.stdin.readline().split('\t')
#y			= Link(input[0], input[1])

def performLinks(linkList, depth, depthMax):
	if (depth < depthMax):
		#print [Link(x) for x in linkList]
		results = [parse(y._wget()) for y in [Link(z) for z in linkList]]
		
		for results, link in zip(results, linkList):
			print results
			results = [normalizeURL(x, link) for x in results]
		pprint.pprint(zip(results, linkList))
		#results = [normalizeURL(result, link) for result in zip(results, linkList)]
		
		#result = [normalizeURL(x.getURL(), x) for x in result]
	return performLinks(results, depth+1, depthMax)

print performLinks(["http://www.google.com", "http://www.reddit.com"], 0, 2)

#if __name__ == "main":
	#pool 		= Pool(proccesses = 4)
	#initial_cond = [google.com]
	#result 	= pool.apply_async()

	#print(result.get(timeout=10))
	#outFile = open("tmp", "w")
	#outFile.writelines(result)

