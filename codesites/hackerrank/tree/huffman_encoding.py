
# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem


out_s = ""

def find_path(cur_node, q):
    if cur_node.left == None and cur_node.right == None:
        return str(cur_node.data)
    if q.pop(0) == '0':
        return find_path(cur_node.left, q)
    else:
        return find_path(cur_node.right, q)
    

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    global out_s
    q = []
    
    out_s = ""
    
    for x in s:
        q.append(x)
    while q:
        out_s += find_path(root, q)
    # print(q, out_s)
    print(out_s)
        
        