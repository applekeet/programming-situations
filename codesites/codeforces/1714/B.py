"""

5
4
3 1 4 3
5
1 1 1 1 1
1
1
6
6 5 4 3 2 1
7
1 2 1 7 1 2 1


"""
from collections import defaultdict

n = int(input())

for y in range(n):
    dd = defaultdict(str)
    a = int(input())
    seq = input().split(" ")

    unique = True

    for u in range(a - 1, -1, -1):
        # print(seq)
        # print(seq[u])
        if seq[u] not in dd.keys():
            dd[seq[u]] = 0
        else:
            unique = False
            break
    # print(a - u, u)
    print(u) if unique else print(u + 1)

