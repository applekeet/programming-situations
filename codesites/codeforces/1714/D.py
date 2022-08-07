"""

6

bababa
2
ba
aba



3
2 2
1 1
2 4






------------------------
caba
2
bac
acab
================


-1



-------------------------------
abacabaca
3
aba
bac
aca
======================

4
1 1
2 6
3 3
3 7




------------------------------
baca
3
a
c
b
=================


4
1 2
2 3
3 1
1 4



-----------------------------
codeforces
4
def
code
efo
forces
=================

2
2 1
4 5



--------------------------
aaaabbbbcccceeee
4
eeee
cccc
aaaa
bbbb
================


4
1 13
2 9
3 1
4 5


"""

n = int(input())

for i in range(n):
    shabd = input()
    number = int(input())

    akshr_list = []
    for j in range(number):
        akshr_list.append(input())

    # akshr_list = akshr_list - missing_akshr_set
    # sort the list by size of akshr
    akshr_list_sorted = sorted(akshr_list, key=len, reverse=True)

    # store the coloring and their points
    l1 = len(shabd)
    output = []
    idx = 0
    old_idx = -1

    # start from start of the word and go till end.
    while idx < l1 - 1:
        # check the item exists
        found = False
        for word in akshr_list_sorted:
            word_length = len(word)
            old_idx = idx
            print("\n----start----", shabd, word, idx, l1 - 1)
            if shabd.find(word, idx) == idx:
                print("--match", idx)
                idx += len(word)
                output.append((akshr_list.index(word) + 1, old_idx))
                found = True
            else:
                in_idx = idx
                found_inside = False
                print(word, idx, in_idx, old_idx)
                while idx != old_idx and idx > 0:
                    idx -= 1
                    print("inside", word, idx, in_idx)
                    if shabd.find(word, idx) == idx:
                        print("--match old", idx)
                        idx += word_length
                        print(idx)
                        output.append(
                            (akshr_list.index(word) + 1, idx - word_length))
                        found_inside = True
                        break
                if not found_inside:
                    idx = in_idx
                    print("keep the idx same", str(idx))

        # at this point no word match at the point
        # take one step back
        if found:
            old_idx = idx - word_length

    print(output)
    print("-----end of answer-----")

    # while l1 != sum(color):
    #     if idx == number:
    #         break
    #     # pt = shabd.find(akshr_list_sorted[idx])
    #     # create generator for finding all occurence
    #     g1 = re.finditer(akshr_list_sorted[idx], shabd)
    #     pt_list = list(g1)
    #     print(pt_list)
    #     for pt in pt_list:
    #         print(akshr_list_sorted[idx], str(pt))
    #         if pt != -1:
    #             exit = False
    #             point_list.append(
    #                 [akshr_list.index(akshr_list_sorted[idx]), str(pt)])
    #     print(point_list)
    #     idx += 1

    # # no item exists in the main string
    # if exit:
    #     print("-1")
    #     continue
