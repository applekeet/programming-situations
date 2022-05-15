def​ ​solution(h,​ ​q):
	# height of the tree = h
	result = []
	for x in q:
		total_elements = (2**h) - 1
		if x >= total_elements:
			result.append(-1)
			continue
		else:
			y = 0
			subtree = total_elements
			flag = True

			while flag:
				subtree = subtree >> 1

				left = y + subtree

				right = left + subtree

				node_point = right + 1

				if left == x or right == x:
					result.append(node_point)
					flag = False
				# number is higher than the left, should be on right
				if x > left:
					y = left
	return result

