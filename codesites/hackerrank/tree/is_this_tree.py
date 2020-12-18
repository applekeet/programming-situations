
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem


prev_value = 0

def checkBST(root):
    global prev_value
    
    if root != None:
        # if this CheckBST(left) is true, this return will not execute
        if not checkBST(root.left):
            return False
        
        if prev_value >= root.data:
            return False
        
        prev_value = root.data
        
        return checkBST(root.right)
    return True


    