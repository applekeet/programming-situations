
# inp = [2, 3, 7, 4, 5]
inp = [8, 7, 7, 7, 8, 8, 5, 6, 3]
# inp = [2, 3, 7, 7, 4, 5]


## funcking google question.. 
# need to fucking speed up.. on this thing.

def l_maxima(inp):
	inp_size = len(inp)
	lm = []
	x = 1
	if inp[0] > inp[1]:
		lm.append(0)

	while x <= inp_size-2:
		print(x, lm)
		flag = 0
		if inp[x-1] < inp[x]:
			if inp[x] > inp[x+1]:
				lm.append(x)
			elif inp[x] == inp[x+1]:
				eq_maxima = []
				for y in range(x, inp_size-2):
					if inp[y] < inp[y+1]:
						x = y+1
						# eq_maxima.clear()
						print(x, y, lm, "found")
						flag = 1
						break
					elif inp[y] == inp[y+1]:
						eq_maxima.append(y)
					else:
						eq_maxima.append(y)
						lm.extend(eq_maxima)
		if flag == 0:
			x = x + 1
	if inp[inp_size-1] > inp[inp_size-2]:
		lm.append(inp_size-1)
	return lm


print(l_maxima(inp))


