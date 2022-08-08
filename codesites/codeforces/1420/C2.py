
q = int(input())

inp_length = []
inp = []


# this incorrect, watch the video
# https://www.youtube.com/watch?v=97tieEKfvBs
for x in range(q):
    n = int(input())
    nums = list(map(int, input().split(" ")))

    ans = 0

    for i in range(n):
        cur = nums[i]
        if i == (n - 1):
            nxt = 0
        else:
            nxt = nums[i + 1]
        ans += max(cur - nxt, 0)

    print(ans)
