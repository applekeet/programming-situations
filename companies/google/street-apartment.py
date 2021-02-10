'''

1 1 1 1 1 1 1

minimise the travel distance



gym: true
school: false
store: false


req = [school, store]


'''

in_blocks = [
	{"gym": False, "school": False, "store": True},
	{"gym": True, "school": False, "store": True},
	{"gym": True, "school": True, "store": False}
]

req = ["school", "store"]

B = len(in_blocks)
R = len(req)

l = []

for i in range(B):
	l.append([])
	for r in req:
		if in_blocks[i][r]:
			l[i].append(0)
		else:
			i1, i2 = i, i
			while True:
				i1 = i1 - 1
				i2 = i2 + 1
				if i1 >= 0 and in_blocks[i1][r]:
					l[i].append(abs(i-i1))
					break
				elif i2 < B and in_blocks[i2][r]:
					l[i].append(abs(i-i2))
					break

print(l)

minimum_distance = []

for one in l:
	minimum_distance.append(max(one))

print(minimum_distance, min(minimum_distance))

