# functions.py
# Bill Campbell 
# Homework 1: Python Recursion
# By Daniel Werminghausen
# 9/08/2016

#######################################################################################################################################

#1.

# In defining function f2c i made the argument (fahrenheit) 
# to make it more understandable to the reader reading this program 
# I used the name f2c name of the function because i had to use it for grading purposes
# I made f2c return any S which is represented by Fahrenheit be returned
# with the conversion of fahrenheit to celcuis which is # -32 * 5/9.
# Under the Function are some test results of the Fahrenheit to Celcuis conversion program
def f2c(fahrenheit):
	'''
	turning fahrenheit into celcuis
	
	Args:
		farenheit (int): The farenheit to be converted to celcius

	Returns:
		float: The return value of the celcius equivilant of the passed in farenheit
	'''
	return (fahrenheit - 32) * (5/9)

#Tests
# print("Testing function f2c() - farenheit to celcius converstion ")
# print("f2c(212) => {}".format( f2c(212) ) )
# print("f2c(40) => {}".format( f2c(40) ) )
# print("f2c(41) => {}".format( f2c(41) ) )
# print("f2c(-40) => {}".format( f2c(-40) ) )
# print("f2c(130) => {} ".format( f2c(130) ) ) 

#######################################################################################################################################

#2.

# I define function dot I made my arguments (listOne, listTwo)
# I use an if statement to ask the function if argument 1 and argument 2 which are (listOne, listTwo)
# have any elements. If yes it goes to the first return and return's argument 1 element[0]  and multiplies
# it by argument 2 element[0]. + Then I add recursion i add function dot and slice out element one out from
# listOne and listTwo and return the it. and this repeats until no more element in listOne or listTwo
def dot(listOne , listTwo):
	'''
	calculate the dot product of two vectors

	Args:
		listOne (list): list of integer
		listTwo (list): list of integers

	Return:
		float: the sum of the products of elements in the same position of the input lists
	''' 
	if listOne and listTwo:
		return (listOne[0] * listTwo[0]) + dot(listOne[1:], listTwo[1:])
	else:
		return 0.0
# Tests
# print("Testing dot function - dot product of two lists")
# print(dot([5,3], [6,4])) #42
# print(dot([5,9], [6,2,5])) #48
# print(dot([4,10], [6,4]))  #64
# print(dot([], []))  #0.0
# print(dot([5], [])) #0.0
# print(dot([3,5,7], [2,5,8])) #87

#######################################################################################################################################

#3.

# In Defining function explode i have one argument (string)
# I use the if statement to ask the function if the argument has any elements 
# Then return a list of argument 1 element one of string[0] and add the function explode(string[1:])
# slice out the first element and return the rest
# explode = "abcde"
# print(list(explode))

def explode(string):
	''' 
	slicing up a string into a list of its characters

	Args:
		string (str): the string to be exploded

	Return:
		list: list of charcaters that nake up the string

	'''
	if string:
		return [string[0]] + explode(string[1:])
	else:
		return []
#Tests:
# print(explode("hello"))
# print(explode("philipp is pro"))

#######################################################################################################################################

#4.

# In defining function ind i named my functions (element and sequence)
# I ask my function if not argument 1 meaning if argument does not have any elements and or argument 2
# if that has any elements equal to argument 1 first element(sequence[0])
# then return 0, else: return 1 + the function ind(element ,sequence[1:]). I slice out the first element in argument sequence

def ind(element , sequence):
	''' 
	Find the index of x in a list

	Args:
		element (mixed): the element for which the index will be found
		sequence (sequence): a sequence to find the element in

	Return:
		int: the index 
	'''
	if not sequence or element == sequence[0]:
		return 0
	else:
		return 1 + ind(element, sequence[1:])
#Tests:
# print(ind(42, [55, 77, 42, 12, 42, 100])) #expected 2
# print(ind(42, range(0,100))) # 42
# print(ind('hi' , [ 'hello' , 42, True])) # 3
# print(ind('hi' , ['well' , 'hi' , 'there' ])) #1
# print(ind('i' , 'team')) #4
# print(ind(' ', 'outer exploration'))# 5

#######################################################################################################################################

#5.

# In defining function removeALL with 2 arguments (lolipop, sequence)
# I use the the if statment asking the function if argument sequence does not have an element
# If yes then it returns and empty list
# elif: argument 1 is equal to argument 2 element 1
# then return function removeAll(lolipop, sequence[1:]) slice element 1 from argument two and return the function
# else: it would put element 1 from argument two in a list + add removeAll(lolipop, sequence[1:]) so same thing as the
# other return
def removeAll(lolipop, sequence):
	'''
	remove all elements in a sequence that match x

	Args:
		lolipop (mixed): the element to be removed from the sequence
		sequence (list): list to be filtered

	Return:
		list: filtered list
	''' 
	if not sequence:
		return []
	elif lolipop == sequence[0]:
		return removeAll(lolipop, sequence[1:])
	else: 
		return [sequence[0]] + removeAll(lolipop, sequence[1:])
#Tests:
# print(removeAll(42,[55, 77,42,11,42,88]))
# print(removeAll('hi',['yo', 'bro','hi','no']))
# print(removeAll(1, [1,2,3,'hi', 'true', True]))

#######################################################################################################################################

#6.

# In defining function myFilter, i have two arguments named predicate and liste.
# I ask my function if there is (not) an element in my argument liste and if that is true it should return an empty list
# elif argument 1 (predicate) and i call out argument 2 (listo element one [0])
# return a list of argument 1 element 1 and use recursion so i call out my function again and slice element 1 out of liste because i dont need it anymore
# else: it should return an empty list and call out the function myFilter and use recursion 

def myFilter(predicate, liste):
	'''
	Filters a list based on a predicate function

	Args:
		predicate (function): a function that returns true or false
		liste (list): the list to be filtered

	Return:
		list: of elements that return True from running through the predicate function
	 '''
	if not liste:
		return []
	elif predicate(liste[0]):
		return [liste[0]] + myFilter(predicate, liste[1:])
	else:
		#first element is odd
		return [] + myFilter(predicate, liste[1:])
#Tests:
# def even(number):
# 	if number % 2 == 0:
# 		return True
# 	else:
# 		return False

# def divBy3(noomba):
# 	if noomba % 3 == 0:
# 		return True
# 	else:
# 		return False
# print(myFilter(even,[1,2,3,4]))
# print(myFilter(divBy3,[2,7,8,10,120,3,9, 90])) 

#######################################################################################################################################

#7.

# In defining function deepReverse i have one argument (listo)
# if not element in argument listo then return an empty list
# elif: element is type list deepReverse again and pass in listo minus the first argument and call deepReverse on the current element
# else just call deepReverse again and pass in listo minus the first argument and the current element to the back
def deepReverse(listo):
	'''
	the reversal of a list and all sub-lists

	Args:
		listo (list): list to be reversed

	Return:
		list: the input list in reverse order
	'''
	if not listo:
		return []
	elif type(listo[0]) == type([]):
		return deepReverse(listo[1:]) + [deepReverse(listo[0])]
	else:
		return deepReverse(listo[1:]) + [listo[0]]
#Tests:
# print(deepReverse([2,3]))
# print(deepReverse([3,[2,3],6]))

#######################################################################################################################################

#8.

# In defining function interset which holds two arguments (list1, list2)
# If no elemnts in list1 or list2 then return an empty list 
# Else if list1 element one is equal to list2 element 1 then return a list of argument 1 element 1 and using recursion 
# + call the function intersect( a list of argument of element 1, and argument 2 slice the first element and return the rest [1:])
# + call the function intersect again and slice off element one from argument 1 and return the rest
# else: 
# return calling the function intersect( a list of argument of element 1, and argument 2 slice the first element and return the rest [1:])
# + call the function intersect again and slice off element one from argument 1 and return the rest
def intersect(list1,list2):
	''' 
	computes the intersection of two sets

	Args:
		list1 (list): set 1
		list2 (list): set 2
	Return:
		list: the intersection of set 1 and set 2
	'''
	if not list1 or not list2:
		return []
	elif list1[0] == list2[0]:
		return [list2[0]] + intersect([list1[0]],list2[1:]) + intersect(list1[1:],list2)
	else:
		return intersect([list1[0]],list2[1:]) + intersect(list1[1:],list2)
#Tests:
# print(intersect([1,2,3],[1,3,5,7])) #[1,3]
# print(intersect([1,[2,3],4],[4,2,[2,3],0])) #[4,[2,3]]
# print(intersect([1,[2,[3,4],[5,[6,7],8]]],[])) #[]

#######################################################################################################################################

#9.

# In defining the function letterscore with two arguments ( letter, and scrabbleScore)
# if no scrabbleScore then return the docstring as seen below
# else if argument 1 is equal to scrabbleScore[0][0] meaning list of [0] which is ["a", 1] and element 0 so "a"
# return scrabbleScore[0][1] meaning list of [0] and return the second element of that list which is always the number
# else: return the function letterScore(letter, scrabbleScore[1:]) so slicing off the first list of the scrabbleScore

scrabbleScores =  [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], 
                 ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], 
                 ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], 
                 ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], 
                 ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

def letterScore(letter, scrabbleScore):
	'''
	Finds score of a character based on a scrabble score list

	Args:
		letter (str): a charcater for which the score needs to be found
		scrabbleScore (list): lists that make up the the scrabble score board

	Return:
		int: the score of the character that needed to be found 

	'''
	if not scrabbleScore:
		return "oh no crash!"
	elif letter == scrabbleScore[0][0]:
		return scrabbleScore[0][1] 
	else:
		 return letterScore(letter, scrabbleScore[1:])
#Tests:
# print(letterScore("a", scrabbleScores))
# print(letterScore("b", scrabbleScores))
# print(letterScore("z", scrabbleScores))
# print(letterScore("g", scrabbleScores))
# print(letterScore("$", scrabbleScores))

#######################################################################################################################################

#10.

# In defining the function wordScore which has two arguments (S, and scrabbleScores)
# if not, any elements in argument scrabbleScores or no elements in argument S
# return 0 (nothing)
# else if S: is argument S has elements then 
# return the function letterScore(return first element of argument one , all of scrabblescores)
# + call function wordScore(S[1], so slice first element out of argument S and return the rest and , return scrabbleScores)
# else: return 0 (nothing)
def wordScore(letter1, scrabbleScores):
	"""
	Calulated scrabble for of a string
	
	Args:
	    letter1 (str): The word to be scored
	    scrabbleScores (list): a list of scores for each charcater
	
	Returns:
	    int: the scrabble score
	"""
	if not scrabbleScores or not letter1:
		return 0
	elif letter1[0] == scrabbleScores[0][0]:
		return scrabbleScores[0][1] + wordScore(letter1[0], scrabbleScores[1:]) + wordScore(letter1[1:], scrabbleScores)
	else:
		return wordScore(letter1[0], scrabbleScores[1:]) + wordScore(letter1[1:], scrabbleScores)


# Tests:
# print(wordScore("spam", scrabbleScores))
# print(wordScore("hahahah", scrabbleScores))