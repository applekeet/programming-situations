
q = int(input())

inp_length = []
inp = []

for x in range(q):
    n = int(input())
    nums = list(map(int, input().split(" ")))

    # two list for max and min..
    mx = (n - 1) * []
    mn = (n - 1) * []

    for i in range(n - 1, -1, -1):
        mx[i] = max(mx[i + 1], nums[i] - mn[i + 1])
        mn[i] = max(mn[i + 1], nums[i] - mx[i + 1])

    print(mx[0])
