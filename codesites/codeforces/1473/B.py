'''

3
baba
ba
aa
aaa
aba
ab


'''

t = int(input())

for x in range(t):
	a = input()
	b = input()

	sub_a = a.find(b)
	sub_b = b.find(a)

	if sub_a:
		print("b is substring")
	if sub_b:
		print("a is substring")

	

