
'''

3
5 3
2 3 2 5 4
3 4
2 4 4
5 4
2 1 5 3 6


'''

t = int(input())

for i in range(t):
	n = int(input())
	x = 0
	while n:
		x += 1
		n = n - 2020
		if n < 0:
			print("NO")
			break
		if n == 0 or n <= x:
			print("YES")
			break


	

