# https://www.hackerrank.com/challenges/torque-and-development/problem

#!/bin/python3

import math
import os
import random
import re
import sys

s = 0 # cities of a component


def create_adj_list(adj_list, n, cities):
    print("cool")
    for x, y in cities:
        adj_list[x].append(y)
        adj_list[y].append(x)
    return adj_list


def helper_DFS(x1, adj_list, visited):
    global s
    s += 1
    visited[x1-1] = True
    for x in adj_list[x1]:
        if not visited[x-1]:
            helper_DFS(x, adj_list, visited)


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    global s
    if c_road >= c_lib:
        # just build library in each city
        return c_lib * n
    # if the cost of library is higher than road
    # loop through the roads to find disjoint sets or connected components
    # total components is number of libraries required
    # total roads is number of cities in one component minus one (c - 1)

    # adj_list = dict.fromkeys(range(1, n))
    adj_list = {x:[] for x in range(1, n+1)}
    # create adj list
    adj_list = create_adj_list(adj_list, n, cities)

    cost = 0

    # find connected componentscost = 0
    visited = [False]*n
    city_cc = []
    for x in range(1, n+1):
        if not visited[x-1]:
            s = 0
            helper_DFS(x, adj_list, visited)
            cost = cost + c_lib
            cost = cost + (c_road*(s-1))
    visited.clear()
    adj_list.clear()
    return cost



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        # fptr.write(str(result) + '\n')
        print(str(result) + '\n')

    # fptr.close()

