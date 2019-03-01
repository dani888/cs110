# recFibonacci.ha
# Bill Campbell 
# Homework 3: HMMMM
# By Daniel Werminghausen
# 10/8/2016

#	r1 Nth fibonacci number
#	r2 N

0	setn r15 100			# Initialize stack pointer
1	setn r1 0				# set initial result to 0
2	read r2 				# read in number from user # get N
3	calln r14 6				# Recursive function finds Nth fibonacci number
4	write r1 				# The result
5	halt					# stop the program

#Recursive fibonacci function
#if n <= 0
6	jgtzn r2 8				# check if r2 is greater than 0 and if yes, jump to line 8
7	jumpr r14				# return the function call
#if n <= 2
8	copy r3 r2				# set register 3 equal to register 2
9	addn r3 -2				# subtract 2 from register 3
10	jgtzn r3 13				# check if register 3 is greater than 0 if yes, jump to line 13
11	addn r1 1				# add 1 to the answer
12	jumpr r14				# return the function call
#if n > 2
#fib(n-1)
13	addn	r15,1			# increment stack pointer
14	storer	r2,r15			# push r2 onto the stack
15	addn	r15,1			# increatse stack counter
16	storer	r14,r15			# push r14 onto stack

17	addn r2 -1				# subtract 1 from register 2
18	calln r14 6				# call the function with (n-1)

19	loadr	r14,r15			# Recover precious possessions
20	addn	r15,-1			# ...
21	loadr	r2,r15			# ...
22	addn	r15,-1			# ...
#fib(n-2)
23	addn	r15,1			# increment stack pointer
24	storer	r2,r15			# push r2 onto the stack
25	addn	r15,1			# increatse stack counter
26	storer	r14,r15			# push r14 onto stack

27	addn r2 -2				# subtract 2 from register 2
28	calln r14 6				# call function with (n-2)

29	loadr	r14,r15			# Recover precious possessions
30	addn	r15,-1			# ...
31	loadr	r2,r15			# ...
32	addn	r15,-1			# ...
#return
33	jumpr r14				# return the function call

