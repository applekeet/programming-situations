T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.sort(reverse = True)
    print(N, arr)
    ops = 0
    for count, num in enumerate(arr):
        if count != 0:
            if num < num2:
                ops += 1
        else:
            num2 = num
        num2 = num
    if arr[-1] != 0:
        ops += 1
    print(ops)

    
