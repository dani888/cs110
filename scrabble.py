# High Order Functions
# Bill Campbell 
# Homework 2:High Order Functions
# By Daniel Werminghausen
# 9/27/16

# from bigdict import * 
scrabbleScore =  [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], 
                 ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], 
                 ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], 
                 ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], 
                 ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]
# rack = ["a", "c", "d", "t", "o"]
######################################################################################################################################################

# 1.)
# the function letterScore uses the built in filter function to filter through scrabble scores to get the score for the letter
# the lambda function that we pass into the filter function only returns true if the letter of the scrabbleScore is the same as the letter we passed in 
# therfor filtering out any other letter score
def letterScore(letter, scrabbleScores):
	'''
	Computes the scrabble score of a character

	Args:
		letter (str): the letter to be scored
		scrabbleScore (list): lists that make up the the scrabble score board

	Return:
		int: the score of the character 
	'''

	return filter(lambda a:a[0][0] == letter, scrabbleScores)[0][1]
print(letterScore("h", scrabbleScore)) # 4
print(letterScore("z", scrabbleScore)) # 10
print(letterScore("i", scrabbleScore)) # 1
######################################################################################################################################################
# 2.)
# the function wordScore uses the built in function reduce and map.
# the map function is used to get the score of each letter in the word
# the reduce function is used used add up all the letter scores
def wordScore(word, scrabbleScore):
	'''
	 Computes the scrabble score of the word
	
	Args:
		word (str): the word to be scored
		scrabbleScore (list): lists that make up the the scrabble score board
	
	Returns:
		int: returns the sum of all the character scores from the word
	 '''
	scores = map(lambda a:letterScore(a, scrabbleScore), word)
	return reduce(lambda a,b:a+b, scores)

# print(wordScore("hello", scrabbleScore)) #4 + 1 + 1 + 1 + 1 = 8
# print(wordScore("zyzzyva", scrabbleScore)) # 4 + 1 = 5
# print(wordScore("happy", scrabbleScore)) # 4 + 1 + 3+ 3 + 4 = 15
######################################################################################################################################################

# 3.) 
# [list comprehensions]
words =[x for x in Dictionary]
twoletterWords =[x for x in Dictionary if len(x) == 2]
lengths = [len(x) for x in Dictionary]
# print(words) #["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]
# print(twoletterWords) # ["am", "at"]
# print(lengths) # [1,2,2,5,3,3,6,3,3,4,6,6]
######################################################################################################################################################
# 4.)
# the function removeFirstInstance is made as a recusive function
# if there is no itterable item left then it should return an empty list
# otherwise if the element is equal to the the first element in itterable. The function will return iterrable without the current first element
# else return a list of the first element of iterrable and add the recursive call of removeFirstInstance with element and iterrable without its first element
def removeFirstInstance(element, iterrable):
	'''
	Removes the first instace of element from the iterrable

	Agrs:
		element (mixed): the element to be removed from itterable
		iterrable (iterrable): iterrable 

	Returns:
		list: returns iterrable with first instance of element removed
	'''
	if not iterrable:
		return []
	elif element == iterrable[0]:
		return iterrable[1:]
	return [iterrable[0]] + removeFirstInstance(element, iterrable[1:])


# print(removeFirstInstance("am", Dictionary)) # ["a", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

# The wordInRack function is made a recursive function
# if there is no word then it should return True
# otherwise if there is a rack and the first character in word is in rack 
# do a recursive call of wordInRack and pass in the rest of the word excluding the first character to check the next character 
# also have to make sure to remove the found character from rack to not use it again
# otherwise if character is not found in rack then return False 
def wordInRack(word, rack):
	"""
	checks if a word can be created given the characters in from rack

	Args:
	    word (str): word 
	    rack (list): a list of characters
	
	Returns:
	    bool: return true or false if the word can be created with the characters in rack
	"""
	if not word:
		return True
	elif rack and word[0] in rack:
		return wordInRack(word[1:],removeFirstInstance(word[0],rack)) 
	return False

# print(wordInRack("spam",["a", "s", "m", "t", "p"])) # True
# print(wordInRack("spamm",["a", "s", "m", "t", "p"])) # False

# The function getvalidWords uses list comprehension to get a list of valid words from Dictionary
def getValidWords(rack):
	"""
	gets all words from dictionary that can be made with the characters of rack 
	
	Args:
	    rack (list): characters in a list
	
	Returns:
	    list: returns a list of words from dictionary if word can be made from rack 
	"""
	return [word for word in Dictionary if wordInRack(word, rack)]

# print(getValidWords(["a", "s", "m", "t", "p"])) # ['a','am','at','spam']

# The function scoreWordList uses the the built in function map to apply the function WordScore to every element in the iterabble
def scoreWordList(wordList):
	"""
	scores all words in wordList

	Args:
	    wordList (list): a list of words
	
	Returns:
	    list: returns a list of lists with words and thier score
	"""
	return map(lambda a:[a, wordScore(a,scrabbleScore)], wordList)

# print(scoreWordList(["dani","is","pro"])) # [['dani',5],['is',2],['pro',5]]

# The function scoreList first gets a list of words from Dictionary that can be made using the charcaters in the rack by calling getValidWords function
# then it scores each word in the list by calling scoreWordList function.
def scoreList(rack):
	"""
	gets and scores all words that can be created from rack
	
	Args:
	    rack (list): a list of characters 
	
	Returns:
	    list: returns a list of lists with words and thier score
	"""
	validWords = getValidWords(rack)
	return scoreWordList(validWords)

# print(scoreList(['a', 'b', 'v', 'x', 'y', 'y', 'z', 'z', 'z'])) # [['ab', 4], ['aby', 8], ['ax', 9], ['ay', 5], ['ba', 4], ['bay', 8], ['by', 7], ['ya', 5], ['yay', 9], ['za', 11], ['zax', 19], ['zyzzyva', 43], ['zzz', 30]]
# print(scoreList(["a", "s", "m", "t", "p"])) # [['a', 1], ['am', 4], ['at', 2], ['spam', 8]]
# print(scoreList(["a", "s", "s", "d"])) # [['a',1]]
# print(scoreList(["a", "s", "m", "o", "f", "o"])) # [['a', 1], ['am', 4], ['foo', 6]]
# print(scoreList(["b", "a", "l", "e"])) # [['am', 4],['a', 1], ['foo', 6]]

# The function bestWord reduces the result of the scoreList function to the highest scoring word
# The lambda function we pass into reduce checks a and b and returns the one with the higher score
def bestWord(rack):
	'''
	 determine the highest scoring word using rack
	
	Args:
	    rack (list): a list of characters

	Returns:
		list: Return the highest scoring word with its score
	'''

	scorelist = scoreList(rack)
	return reduce(lambda a,b: a if a[1] > b[1] else b, scorelist)


print(scoreList(["a", "s", "m", "t", "p"]))
print(bestWord(["a", "s", "m", "t", "p"])) # [['spam',8]]

print(scoreList(["a", "t", "m", "p", "a"]))
print(bestWord(["a", "t", "m", "p", "a"])) # [['am', 4]]

print(scoreList(["a", "s", "m", "t", "p"]))
print(bestWord(["a", "s", "m", "t", "p"])) # [['spam', 8]]



######################################################################################################################################################