
n = int(input())

inp_length = []
inp = []

for x in range(n):
    nums_length = int(input())
    nums = list(map(int, input().split(" ")))

    sorted1 = True

    for i in range(nums_length - 1):
        if nums[i] <= nums[i + 1]:
            sorted1 = False
            break

    if sorted1:
        print("NO")
    else:
        print("YES")





    