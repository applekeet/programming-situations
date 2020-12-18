
# https://www.hackerrank.com/challenges/balanced-forest/problem
# 

def create_adj_list(adj_list, edges):
    print("cool")
    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)
    return adj_list


def helper_DFS(x1, adj_list, visited, c):
    sums = []
    
    visited[x1-1] = True
    # is false in visited; add those numbers to sums
    for x in adj_list[x1]:
        sums.append()
        if not visited[x-1]:
            helper_DFS(x, adj_list, visited)

# Complete the balancedForest function below.
def balancedForest(c, edges):
    print(c, edges)
    adj_list = []
    adj_list = create_adj_list(adj_list, edges)
    sums = helper_DFS(1, adj_list, c)
    
    

