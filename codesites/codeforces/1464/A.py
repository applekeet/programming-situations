'''
4 5
5 1
2 2
3 3


_ _ _ x _
x _ _ _ _
_ x _ _ _
_ _ _ _ _
_ _ x _ _


'''

def run(n, m, rooks):
	flag = 0
	for r in rooks:
		if r[0] == r[1]:
			m -= 1
	for r in rooks:
		for r1 in rooks:
			if r[0] == r1[1]:
				flag = 1
				break
		if not flag:
			break
	return m+1 if flag else m
				

t = int(input())

for _ in range(t):
	n, m = input().split() # n size of board, m number of rooks
	rooks = []
	for pos in range(int(m)):
		x1, y1 = input().split()
		rooks.append([int(x1), int(y1)])
	print(run(int(n), int(m), rooks))

