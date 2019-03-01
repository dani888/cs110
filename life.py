# life.py
# Bill Campbell 
# Homework 4: Conway's Game Of Life
# By Daniel Werminghausen
# 10/22/2016

import sys
import random
import ast
###########################################################################################################
# The function createOneRow has one argument width:
# for any column in range width return row of cells   
def createOneRow(width):
    """returns one row of zeros of width "width"  
    
    Args:
        width (int): width of the row
    return:
    	list: a list of dead cells
    """
    row = []
    for col in range(width):
        row += [0]
    return row
    #return [0 for x in range(width)]

# The function createBoard has two arguments width and height:
# this time its oppsite to createOneRow. for any row in 
# range of height.
# returns a board of 0's depending on width and hieght of board 
def createBoard(height, width):
    """returns a 2d array with "height" rows and "width" cols 
    
    Args:
        width (int): width of the row
        height (int): hieght of the column

    return:
    	list: lists of  of dead cells depending on what number
    	we plug in for width and height
    """
    A = []
    for row in range(height):
        A += [createOneRow(width)]    
    return A
    #return [createOneRow(width) for x in range(height)]

# print(createBoard(5, 3))
###########################################################################################################

# The function printBoard has one argument A:
# prints  board (becomes the new print function. Instead of
# print to run a function we use printboard to print our
# results in a 2d array.
def printBoard( A ):
    """this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    
    Args:
        A (list): a 2d array of dead cells [0]

    return:
    	list: a board,  2d board list-of-lists
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

# The function printBoard2 has one argument A:
# print board using @ (is the samne as printBoard)
def printBoard2( A ):
    """this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    
    Args:
        A (int): a 2d array of dead cells 

    return:
    	list:a board,  2d board using @
    """
    for row in A:
        for col in row:
        	if col == 1:
        		sys.stdout.write("@")
        	else:
        		sys.stdout.write(" ")
        sys.stdout.write( '\n' )

# printBoard(createBoard(5, 3))
###########################################################################################################

# The function diagonalize has two arguments width and height:
# for row in range of height and for col in range of width
# if row is equal to col then return as a live cell 1
# else return a dead cell 0
def diagonalize(width,height):
    """creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    
    Args:
        width (int): width of the row
        height (int): height of column

    return:
    	list: 2d board modified so it has a diagonal
    	strip of live cells
    """
    A = createBoard(height, width) 
    
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0     

    return A

# printBoard(diagonalize(10, 5))
###########################################################################################################
# The function innerCells has two argument width and height:
# creates a board that is filled with live cells, the outside is dead cells
def innerCells(width, height):
	"""creates ......
	
	Args:
	    width (int): width of the row
	    height (int): height of column

	return:
		list: a list of lists with alive cells in a one-cell-wide border of empty cells
	"""
	A = createBoard(height, width)

	for row in range(height):
		for col in range(width):
			if row > 0 and row < height-1:
				if col > 0 and col < width-1:
					A[row][col] = 1     

	return A

# printBoard(innerCells(5, 6))
###########################################################################################################
# The function randomCells has two arguments width and height:
# A becomes a vairable for createBoard(width,height) just to 
# make testing the function more simple This function checks the 
# range for height and width and checks if row and col are live or dead
# cells and if they are inside a one-cell-wide border of empty cells
# we use import random* to be able to use random.choice and give 
# it the choices of choosing [0,1] randomly 
def randomCells(width, height):
	"""creates an empty board and then modifies it
	so that it has a diagonal strip of "on" cells.
	
	Args:
	    width (int):  width of the row
	    height (int): height of column

	return:
		list: a list of lists with random cells either alive or dead in a one-cell-wide border of empty cells
	"""
	A = createBoard(height, width)

	for row in range(height):
		for col in range(width):
			if row > 0 and row < height-1:
				if col > 0 and col < width-1:
					A[row][col] = random.choice([0,1])     

	return A

# printBoard(randomCells(10,10))
###########################################################################################################

# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# The function copy has one argument board:
# This functions checks the length of width and height
# create a varable for createBoard to give it a new name newBoard
def copy(board):
	"""
	This function basically copy's any board
	you are printing by calling in copy 
	
	Args:
	    board (list): a 2d array of cells

	return"
		list: a copied 2d array of board
	"""
	height = len(board)
	width = len(board[0])
	newBoard = createBoard(height, width)
	for row in range(height):
		for col in range(width):
			newBoard[row][col] = board[row][col]
	return newBoard

# a = randomCells(5,10)
# printBoard(a)
# printBoard(copy(a))
###########################################################################################################
# The function inneReverse has one argument board:
# fist check the width length of board and the height
# for column in range of height"
# if board[row][col] is equal to 1 a live cell, then change it into a dead cell
# else if board[row][col] = 0 a dead cell then change it into a dead cell 0
def inneReverse(board):
	"""
	This function calls in a function like diagonalize and reverses the
	board all live cells turn dead and all dead cells turn live
	
	Args:
	    board (list): a 2d array of cells

	return:
		list: a list of lists of cells that reverse: if the cell is dead it becomes live
	"""
	height = len(board)
	width = len(board[0])
	for row in range(height):
		for col in range(width):
			if board[row][col] == 1:
				board[row][col]=0
			elif board[row][col] == 0:
				board[row][col]=1
	return board
# printBoard(inneReverse(diagonalize(8,10)))
###########################################################################################################
# The function howManyNeigbors has three arguments board,row,col:
# neigbors is a varaible set to 0
# checks the upper left, upper, upper right, left, right, lower left, lower, lower right cells around the live cells
def howManyNeigbors(board,row,col):
	"""all if statments in this function check all possibilities
	   of neigbors assuming a one-cell-wide border of empty cells around it
	
	Args:
	    board (list): a 2d array of cells
	    row (int): width of the row
	    col (int): height of the colum  
   
	Return:
	    list: a list of lists checking if a live cells has neigbors assuming a one-cell-wide border of empty cells around it
	"""
	neigbors = 0
	if board[row-1][col-1] == 1:
		neigbors += 1
	if board[row-1][col] == 1:
		neigbors += 1
	if board[row-1][col+1] == 1:
		neigbors += 1
	if board[row][col-1] == 1:
		neigbors += 1
	if board[row][col+1] == 1:
		neigbors += 1
	if board[row+1][col-1] == 1:
		neigbors += 1
	if board[row+1][col] == 1:
		neigbors += 1
	if board[row+1][col+1] == 1:
		neigbors += 1
	return neigbors
###########################################################################################################
# The function next_life_generation has one argument board:
# fist check the width length of board and the height
# for column in range of height and row in range of width:
# if row is greater than 0 and is inside the one-cell-wide border of empty cells
# we plug in the rules of the Game Of Life if cellNeigbors is less than 2:
# then it will die in next gen
# else if cellNeigbors is greater than 3 it will die 0
# else if cellNeigbors is equal to 3 and board[row][col] is equal to 0
# next gen will will revive the dead cell esle stay the same
def next_life_generation(board):
	"""makes a copy of A and then advanced one
	generation of Conway's game of life within
	the *inner cells* of that copy.
	The outer edge always stays 0.
	
	Args:
	    board (list): a 2d array of cells

	return:
		list: list of lists checking Conways game of life rules
	"""
	height = len(board)
	width = len(board[0])
	nextGen = copy(board)
	for row in range(height):
		for col in range(width):
			if row > 0 and row < height-1:
				if col > 0 and col < width-1:
					cellNeigbors = howManyNeigbors(board,row,col)
					if cellNeigbors < 2:
						nextGen[row][col] = 0
					elif cellNeigbors > 3:
						nextGen[row][col] = 0
					elif cellNeigbors == 3 and board[row][col] == 0:
						nextGen[row][col] = 1
					else:
						nextGen[row][col] = board[row][col]
	return nextGen


# A = [ [0,0,0,0,0,0],
#       [0,0,1,0,0,0],
#       [0,1,0,0,0,0],
#       [0,0,1,0,0,0],
#       [0,0,0,0,0,0]]

# printBoard(A)
# A2 = next_life_generation( A )
# printBoard(A2)
# A3 = next_life_generation( A2 )
# printBoard(A3)
###########################################################################################################
# The function interact has no arguments:
# This is for the menu
# start off with raw_input and give it differnt commands depending
# on the letter we pass into raw imput
# Commands:
# n	[height,width] (Create a height * width board)
# i	(initialize life)
# p	(print the board)
# s	(display the board)
# r	(advance n generations, displaying each after)
# h	(display this help reminder)
# q ends the game of life and prints "Life is over"
def interact():
	"""Interact with a user to play Conway's Game of Life.

	Args: None

	return:
		str:raw_input("Enter Command (h for help): enter command to interact!
	"""
	board = None
	line = raw_input("Enter Command (h for help): ")
	line = line.replace(" ", "")
	while line and line[0] != "q":
		command = line[0]
		if command == 'n':     
			coordinates = ast.literal_eval(line[1:])
			rows = coordinates[0]
			cols = coordinates[1]
			board = createBoard(int(rows),int(cols))
		elif command == 'i':
			liveCells = ast.literal_eval(line[1:])
			for cells in liveCells:
				board[cells[0]-1][cells[1]-1] = 1
		elif command == 'p':
			printBoard(board)
		elif command == 'r':
			numOfGens = ast.literal_eval(line[1:])
			for n in range(numOfGens):
				board = next_life_generation(board)
				printBoard2(board)
		elif command == 's':
			printBoard2(board)
		elif command == 'd':
			printBoard2(board)
		elif command == 'h':
			print(""" 
Commands:
n	[height,width] (Create a height * width board)
i	(initialize life)
p	(print the board)
s	(display the board)
r	(advance n generations, displaying each after)
h	(display this help reminder)

q	(quit)""")
		line = raw_input("Enter Command (h for help): ")
		line = line.replace(" ", "")
	print "Life is over\n"

interact()