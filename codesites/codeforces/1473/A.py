
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
	n, d = input().split()
	a = list(map(int, input().split()))
	flag = 1
	all_small = False

	for i in a:
		if i <= int(d):
			all_small = True
		else:
			all_small = False
			break
	if all_small:
		print("YES")
		continue

	for x in range(int(n)):
		for y in range(x+1, int(n)):
			if a[x]+a[y] <= int(d):
				print("YES")
				flag = 0
				break
		if flag == 0:
			break
	if flag == 1:
		print("NO")

