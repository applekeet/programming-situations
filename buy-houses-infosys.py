"""

input  string

3 2#2 5 6

out:
15

3 3#2 5 6

out:
13

"""

str = input()

a = []
b = []
c = []
a = str.split('#')

b = a[0].split(' ')
c = a[1].split(' ')

N = int(b[0])
K = int(b[1])

arr = list(map(int, c))
arr.sort(reverse=True)

cost = []
for i in range(K):
	cost.append(0)

bought = []
for i in range(K):
	bought.append(0)

sum = 0
if N<=K:
	for i in range(N):
		sum = sum + arr[i]

else:
	for house in range(N):
		for friend in range(K):
			cost[friend] = (bought[friend] + 1) * arr[house]


		minimum = cost[0]
		fri = 0
		print(cost)

		for friend in range(K):
			if cost[friend] < minimum:
				minimum = cost[friend]
				fri = friend
				
			print(minimum)
			bought[fri] = bought[fri] + 1
			print(bought)

		sum = sum + minimum

print(sum)
