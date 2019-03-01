# loopFibonacci.ha
# Bill Campbell 
# Homework 3: HMMMM
# By Daniel Werminghausen
# 10/8/2016

0	read r1					# read in number from user
1	jltzn r1 15				# if register 1 is 0 then jump to line 

2	setn r2 0				# secondToLastNumber
3	setn r3 0				# lastNumber

4	jeqzn r1 13				# Jump to print final Fibonacci
5	addn r1 -1				# subtract 1 from register one
6	jnezn r3 9				# Jump to compute next Fibonacci

7	setn r3 1				# set last number to 1
8	jumpn 4 				# loop back to line 4

9	copy r4 r2				# set tempNumber equal to secondToLastNumber
10	copy r2 r3				# set seondToLastNumber equal to lastNumber
11	add r3 r3 r4			# add tempNumber to lastNumber
12	jumpn 4					# loop back to line 4

13	write r3				# print lastNumber
14	halt 					# stop the program

15	setn r1 0				# set register 1 to 0
16	write r1				# write out register 1
17	halt					# stop the program