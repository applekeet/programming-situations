
n = int(input())

inp_length = []
inp = []

for x in range(n):
    nums_length = int(input())
    nums = list(map(int, input().split(" ")))

    count = 0
    cnt = 32 * [0]

    for i in range(nums_length):
        bit = 0
        # count the leading zeros of number in binary
        while (1 << (bit + 1)) <= nums[i]:
            bit += 1

        # (1 << bit) is the highest power of 2 <= nums[i]
        cnt[bit] += 1

    for x in range(32):
        count += cnt[x] * (cnt[bit] - 1) / 2

    print(count)
