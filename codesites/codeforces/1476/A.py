
'''


4
1 5
4 3
8 8
8 17


[2 2 2 2 2 2 2 3]

[1 1 1 1] > 3
[2 2 2 2] > 3

4 8


'''

t = int(input())

for i in range(t):
	n, k = list(map(int, input().split()))
	if k<n:
		if n%k==0:
			k = n
		else:
			k = (n//k + 1)*k
	if k%n == 0:
		print(k//n)
	else:
		print(k//n + 1)




	

