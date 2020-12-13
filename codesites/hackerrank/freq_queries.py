#!/bin/python3

# https://www.hackerrank.com/challenges/frequency-queries/problem

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    arr = []
    out = []
    for x in queries:
        if x[0] == 1:
            arr.append(x[1]) 
        elif x[0] == 2:
            if x[1] in arr:
                arr.remove(x[1])
        else:
            di = defaultdict(int)
            se = set() ## values with have occurence exactly x[1]
            for num in arr:
                di[num] += 1
                if di[num] == x[1]:
                    se.add(num)
                elif di[num] > x[1]:
                    se.remove(num)
            if se:
                out.append(1)
            else:
                out.append(0)
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
