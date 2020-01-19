num1 = int(input())


while num1:

    #p = input()
    #h = input()

    p = "one"
    h = "zzonneyy"

    list_p = [char for char in p]

    set_p = set(list_p)
    print(len(set_p))
    hash_p = {}
    hash_h = {}

    print(hash_p)

    for letter_in_h in h:
        if letter_in_h in hash_h:
            hash_h[letter_in_h] += 1
        else:
            hash_h[letter_in_h] = 1

    for letter_in_p in p:
        if letter_in_p in hash_p:
            hash_p[letter_in_p] += 1
        else:
            hash_p[letter_in_p] = 1

    print(hash_p, hash_h)

    for one_l in hash_p:
        if one_l in hash_h:
            if hash_h[one_l] >= hash_p[one_l]:
                print("yes")
            else:
                print("no")
        else:
            print("coould not")
            break

    num1 -= 1
