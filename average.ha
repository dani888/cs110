 # average.ha
# Bill Campbell 
# Homework 3: HMMMM
# By Daniel Werminghausen
# 10/8/2016

0	setn r3 -1		# set register 3(r3) = -1 to use as a counter
1	setn r2 0		# set register 2(r2) = 0 to used to sum up all the input numbers. the sum of all numbers
2	read r1			# read user input number into register 1(r1)
3	addn r3 1		# add 1 to register 3 (incrument the counter)
4	add r2 r1 r2	# add the input number to register 2
5	jnezn r1 2		# if register 1 is not equal to 0 then jump to line 2
6	div r4 r2 r3	# devide the sum of all numbers by the register 3 the count of total numbers
7	mod r2 r2 r3	# returns the remainder of the interger devision r3 devided by r2
8	write r4		# prints average rounded down
9	write r2		# prints the remainder
10	halt			# stops the program

