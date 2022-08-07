
n = int(input())

inp_length = []
inp = []

for x in range(n):
    l1_length = int(input())
    l1 = list(map(int, input().split(" ")))
    # inp.append(l1)

    print(l1, l1_length)

    # l1 list has elements..
    l1 = list(set(l1))
    l1.sort()

    print(l1)

    for x in l1:
        z = 10
        while z != 0:
            print(x)
            x = x + (x % 10)
            z -= 1
        print(x, "\n------------")


