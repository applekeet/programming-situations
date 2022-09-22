#!/bin/python3

## https://www.hackerrank.com/challenges/find-the-nearest-clone/

import math
import os
import random
import re
import sys
from collections import defaultdict
import itertools

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
stack = []

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    print(graph_nodes, graph_from, graph_to, ids, val)
    
    # finding the same color destination nodes
    same_color_destination = []
    for x in range(graph_nodes):
        if ids[val-1] == ids[x] and x != (val-1):
            same_color_destination.append(x+1)
    print(val, same_color_destination)
    
    # checking if same color destination do not exist
    if not same_color_destination:
        return -1
    
    # checking if direct path exists between source and destination
    for index, x in enumerate(graph_from):
        if val == x:
            for dest in same_color_destination:
                if dest == graph_to[index]:
                    return 1
    
    adjacency_list = defaultdict(list)
    for x, y in zip(graph_from, graph_to):
        adjacency_list[x].append(y)

    print(adjacency_list)
    
    ## solving for shortest path and length here...
    # Mark all the vertices as not visited
    visited =[False]*(graph_nodes)

    # Create a queue for BFS
    queue=[]

    # Mark the source node as visited and enqueue it
    queue.append(val)
    visited[val] = True

    while queue:

        #Dequeue a vertex from queue
        n = queue.pop(0)
             
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
