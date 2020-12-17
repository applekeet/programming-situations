

'''

def fib(x):
	if x == 0 or x == 1:
		return 1
	return fib(x-1)+fib(x-2)

'''

def fib(x, memo={}):
	if x == 0 or x == 1:
		return 1
	if x in memo:
		return memo[x]
	memo[x] = fib(x-1, memo)+fib(x-2, memo)
	return memo[x]


print(fib(0))
print(fib(1))
print(fib(4))
print(fib(10))
print(fib(20))
print(fib(100))




