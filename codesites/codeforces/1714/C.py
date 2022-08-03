
n = int(input())

for z in range(n):
    a = int(input())

    number_list = []
    x = 9

    if a < 10:
        print(a)
    else:
        while a > 0:
            if a > x:
                number_list.insert(0, x)
            else:
                number_list.insert(0, a)
            a = a - x
            x -= 1
            # print(number_list)
        print("".join(list(map(str, number_list))))
