
# special xor for xor(16, 17, 18) = xor(1...18) - xor(1...15)
# also 1...n xor is either 0, 1, n, n+1
# combine both :P

def special_xor(n):
	x = n%4
	if x == 0:
		return n
	if x == 1:
		return 1
	if x == 2:
		return n+1
	return 0


def solution(start, length):
	cuts = length
	xors = []
	while cuts:
		print(start+cuts-1, start-1, cuts, xors)
		if start == 0:
			xors.append(special_xor(cuts-1))
		else:
			xors.append(special_xor(start+cuts-1) ^ special_xor(start-1))
		start += length
		cuts -= 1
	print(xors)
	some = reduce(lambda x, y: x^y, xors)
	return some

print(solution(0, 3))
print(solution(17, 4))
