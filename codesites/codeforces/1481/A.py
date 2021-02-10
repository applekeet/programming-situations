"""




"""

t = int(input())

for _ in range(t):
	x, y = list(map(int, input().split()))
	s = input()
	flag = 0
	
	R = s.count('R')
	L = s.count('L')
	U = s.count('U')
	D = s.count('D')

	if x > 0 and (x == R or x >= R-L):
		flag = 1
	elif x <= 0 and (abs(x) == L or abs(x) >= L-R):
		flag = 1
	if y <= 0 and (abs(y) == D or abs(y) >= D-U) and flag == 1:
		print("YES")
		continue
	elif y > 0 and (y == U or y >= U-D) and flag == 1:
		print("YES")
		continue
	print("NO")




