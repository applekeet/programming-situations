# height of tree

# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

''' recursive

def height(root):
    if root is None:
        return -1
    else:
        left_h = height(root.left)
        right_h = height(root.right)
        return left_h+1 if left_h > right_h else right_h+1

'''
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# iterative

from collections import deque

def height(root):
	h = -1 # height of tree
	q = deque() # queue in python
	q.append(root)  # add root to the queue to start
	while len(q) != 0: # end condition:: queue is empty
		# number of elements added to the queue in previous iteration
		size_one_row = len(q)
		# loop all the elements of one level
		while size_one_row != 0:
			# pop element from queue and add its children
			rt = q.popleft()
			if rt.left:
				q.append(rt.left)
			if rt.right:
				q.append(rt.right)
			# decrease the number of pops remaining
			size_one_row -= 1
		h += 1
	return h


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))