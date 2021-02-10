
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}


# create new list for answer..
def dirReduc(arr):
	new = []
	for x in arr:
		if new and new[-1] == opposite[x]:
			new.pop()
		else:
			new.append(x)
		print(new)
	return new

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a)) #  ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
# print(dirReduc(u)) # ["NORTH", "WEST", "SOUTH", "EAST"])

