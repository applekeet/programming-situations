#
# https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/roy-and-rangoli-1/
# 
#
#
from random import randint

# Prime nos. to be found till N
n = int(input())



# if n > 100:
	# this is comment.
	# unavailability of good info to make comment


# taking each random number at a time
for i in range(2, n):
	z = 0
	# looping random no. of times like 11
	for j in range(1,12):
		# random integer b/w 2 to 9
		r = randint(1,n-1)
		f = (r**(i-1))%i

		print(f, r, j)

		if f is 1:
			z+=1
			jt = r+1
			print(jt, z)
		else:
			# print(i, " composite ", f)
			print(" ")
	if z is 10:
		print(i, " is a Prime number")
	else:
		print(z, "this is z", i)





		



