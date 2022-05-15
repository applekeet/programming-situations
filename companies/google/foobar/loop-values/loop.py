def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return "".join(digits[::-1])


def baseToNumber(x, b, sizez):
	number = 0
	for i in range(1, sizez + 1):
		number += int(x[sizez - i]) * (b**(i-1))
	return number

def solution(n, b):
	items = []
	looped = []

	while True:
		# make each number using increasing and decreasing order
		a1 = "".join(sorted(n))
		a2 = "".join(sorted(n, reverse=True))

		# size of the string/numbers
		sizez = len(n)
		
		if b == 10:
			z = str(abs(int(a1) - int(a2))).zfill(sizez)
		else:
			# convert numbers from the base to the 10-base for subtraction
			n1 = baseToNumber(a1, b, sizez)
			n2 = baseToNumber(a2, b, sizez)
			z = numberToBase(abs(n1-n2), b).zfill(sizez)

		if z not in items:
			items.append(z)
		else:
			if z not in looped:
				looped.append(z)
			else:
				print("looping", items, looped, len(looped))
				break
		n = z
	return len(looped)

solution("210022", 10)
solution("1211", 10)

