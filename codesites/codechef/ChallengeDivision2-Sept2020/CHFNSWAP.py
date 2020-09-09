T = int(input())

for _ in range(T):
    N = int(input())
    L = list(range(1, N+1))
    addition = (N(N+1))/2
    if (addition % 2) != 0:
        print("0")
        continue
    first_sum = 0
    position = 0
    for count, i in enumerate(L):
        # print(i)
        first_sum += i
        if first_sum >= (addition/2):
            first_sum = first_sum - i
            position = count
            break
    print(N - count)






'''
1 2 3 4

odd addition

2  1 another 

1 2 3 4 5 6 7 8 9 10 11 | 12 13 14 15 16

1 2 3 4 5 6 7 8 9 12 11 | 10 13 14 15 16

------------------------------
1 2 3 4 5 6 7 8 9 10 11 | 12 13 14 15 16
                     66

66 -> 68 -> 2

2

1 2 3 4 5 6 7 8 9 10 | 11 12 13 14 15 16
                  55

55 -> 68 -> 13

3

1 2 3 4 5 6 7 8 9 | 10 11 12 13 14 15 16
                46

46 -> 68 -> 22

136


1 2 3 4 5 6 7 8 9 10 11 12 13 | 14 15 16 17 18 19
                           91
1 2 3 4 5 6 7 8 9 10 11 12 | 13 14 15 16 17 18 19
                        78

78 -> 95 -> 17
91 -> 95 -> 4
'''


