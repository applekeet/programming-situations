# https://app.codility.com/c/run/cert5PTJNT-MEY83Z3BRN8CMEYY/

H = [45,46,47,48,49,50]


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    maxB = max(H)
    finalArea = 0
    if H[0] == H[-1] == maxB:
        return H[0]*len(H)

    maxB2 = 0
    totalbuilding = len(H)
    marker = []
    for count, b in enumerate(H):
        if b == maxB:
            marker.append(count)

    finalArea = len(H[marker[0]:marker[-1]+1]) * H[marker[0]]
    maxB2left = 0
    maxB2right = 0

    print(finalArea, H[marker[-1]+1:])

    if marker[0] != 0:
        maxB2left = max(H[:marker[0]]) * len(H[:marker[0]])
    if marker[-1] != (totalbuilding-1):
        maxB2right = max(H[marker[-1]+1:]) * len(H[marker[-1]+1:])
        
    if marker[0] == 0 or marker[-1] == (totalbuilding-1):
        print(True)
        finalArea = finalArea + maxB2left + maxB2right
        return finalArea

    if maxB2left <= maxB2right:
        area = maxB * len(H[marker[-1]+1:])
        area2 = maxB2left
    else:
        area = maxB * len(H[:marker[0]])
        area2 = maxB2right

    finalArea = finalArea + area + area2
    return finalArea


print(solution(H))
