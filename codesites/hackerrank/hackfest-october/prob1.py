#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def rotate(s, d):
    lf = s[0:d]
    lr = s[d:]
    return lr+lf

def maximumPower(s):
    while s[0] == 0:
        s = rotate(s, 1)
        # print(s)
    for i in range(len(s), 0, -1):
        ss = ""
        x = ss.zfill(i)
        # print(i, ss, x, s)
        # print(s.find(x))
        if x in s:
            return i
    return 0
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "111"

    result = maximumPower(s)

    print(str(result) + '\n')
