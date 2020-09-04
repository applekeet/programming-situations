T = int(input())

for _ in range(T):
    N = int(input())
    M = []
    for _ in range(N):
        arr = list(map(int, input().rstrip().split()))
        M.append(arr)
    # arr.sort(reverse = True)
    print(N, M)