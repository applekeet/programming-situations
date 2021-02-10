
'''

3
5 3
2 3 2 5 4
3 4
2 4 4
5 4
2 1 5 3 6


'''

dvsr = [3,5,7,11,13,17,23]

t = int(input())

for i in range(t):
	n = int(input())
	if n % 2 != 0:
		print("YES")
		continue
	if n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0 or n % 13 == 0 or n % 17 == 0 or n % 23 == 0:
		print("YES")
		continue
	print("NO")




