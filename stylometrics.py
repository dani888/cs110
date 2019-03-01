# stylometrics.py
# Bill Campbell 
# Homework 5:stylometrics
# By Daniel Werminghausen
# 11/13/2016


#################################################################################

def createDictionary(file, dictCounts):
	"""
	This function reads in a file and takes out
	all the symbols which are unnecessary symbols.
	The function counts up how many of each word is used
	Args:
	    file (txt): reads in books 
	    dictCounts (dict): creates a dictionary after having 
	    gone through the function
	
	Returns:
	    dict: a dictionary with each word as the key and 
	    the number of times it comes fourth in the books
	"""
	text = open(file, 'r').read()
	text = text.lower()
	for ch in '!"#$%^&()*=,-./:;<=>?@[\\]^_`{|}~':
		text = text.replace(ch, ' ')
	words = text.split()
	for w in words:
		dictCounts[w] = dictCounts.get(w,0) + 1
	return dictCounts
#################################################################################

def top50Ratios(dictCounts):
	"""
	Takes the created dictionary finds the 50 most
	used words in the book and returns thier ratio's
	
	Args:
	    dictCounts (dict): a dictionary of key(words) in books
	    and the ratio compared to the entire book
	
	Returns:
	    dict: gives the top 50 most used words by the author sorted
	"""
	length = reduce(lambda a,b:a+b,[dictCounts[key] for key in dictCounts])
	ratioDict = dict()
	for key in sorted(dictCounts, key=dictCounts.get, reverse=True)[:50]:
  		ratioDict[key] = dictCounts[key] / float(length)
  	return ratioDict
#################################################################################

def printSortedRatio(ratioDict):
	"""
	Prints the the sorted ratio of ratioDict
	
	Args:
	    ratioDict (dict): a dictionary with the top 50 most used 
	    words by the author
	
	Returns:
	    dict: a dictionary with the top 50 most used words by the author sorted
	"""
	for key in sorted(ratioDict, key=ratioDict.get, reverse=True)[:50]:
  		print key, ratioDict[key]
#################################################################################

def compareScore(dict1, dict2):
	"""
	Compares the dictionary score of dict1 and dict2
	compares the score between the two authors
	Melville or shakespeare
	
	Args:
	    dict1 (dict): dictionary of melville with the top 50 most used words
	    dict2 (dict): dictionary of shakespeare with the top 50 most used words
	
	Returns:
	    dict: a dictionary comparing score of each key in dict1 and dict2
	"""
	score = 0
	for key in dict1:
		if key in dict2:
			score = score + abs(dict1[key] - dict2[key])
	return score
#################################################################################

def identifyAuthor(file):
	"""
	A function that indentify's a book or text
	to see if its by the author Melville or
	Shakespeare or niether of thos two authors
	
	Args:
	    file (txt): a txt file of the book we want to run
	    through the indentify author function
	
	Returns:
	    str: It returns a string for the Melville with thevscore
	    and the same for Shakespeare and return a string of author
	    depending on the score
	"""
	dictonary = dict()
	dictCounts = createDictionary(file,dictonary)
	dictRatio = top50Ratios(dictCounts)
	shakespeareScore = compareScore(dictRatio,shakespeare)
	melvilleScore = compareScore(dictRatio, melville)
	# print("shakespeareScore",shakespeareScore)
	# print("melvilleScore",melvilleScore)
	if shakespeareScore < 0.08:
		return "Shakespeare"
	elif melvilleScore < 0.114:
		return "Melville"
	else:
		return "unknown"

#################################################################################
melville = dict()
melville = createDictionary("moby.txt", melville)
melville = createDictionary("bartley.txt", melville)
melville = createDictionary("omoo.txt", melville)
melville = top50Ratios(melville)

shakespeare = dict()
shakespeare = createDictionary("macbeth.txt", shakespeare)
shakespeare = createDictionary("othello.txt", shakespeare)
shakespeare = createDictionary("allswell.txt", shakespeare)
shakespeare = top50Ratios(shakespeare)

#################################################################################
# printSortedRatio(shakespeare)
# printSortedRatio(melville)
print(identifyAuthor("moby.txt"))
print(identifyAuthor("Bartley.txt"))
print(identifyAuthor("omoo.txt"))
print(identifyAuthor("macbeth.txt"))
print(identifyAuthor("othello.txt"))
print(identifyAuthor("allswell.txt"))


print(identifyAuthor("random1.txt"))
print(identifyAuthor("random2.txt"))
print(identifyAuthor("random3.txt"))
print(identifyAuthor("random4.txt"))
print(identifyAuthor("random5.txt"))
print(identifyAuthor("random6.txt"))
print(identifyAuthor("random7.txt"))



