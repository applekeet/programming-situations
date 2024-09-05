'''

on call rotation of the people is given, 

name, start time, end time

I, 1, 10
J, 5, 7
K, 6, 12
L, 15, 17

Output:

start, end, names
1, 5, I
5, 6, [I, J]
6, 7, [I, J, K]
7, 10, [I, K]
10, 12, [K]
15, 17, [L]

'''

_input = [
    ("I", 1, 10),
    ("J", 5, 7),
    ("K", 6, 12),
    ("L", 15, 17),
]


def rotation(_input):
    startTimes = []
    endTimes = []
    for x in _input:
        startTimes.append(x[1])
        endTimes.append(x[2])
    print(endTimes, startTimes)
    startTimes.sort()
    endTimes.sort()

    _output = []

    i, j = 0
    while i + j < range(2 * len(_input)):
        if startTimes[i] < endTimes[j]:
            i += 1
        else:
            j += 1

    ## kya bakchodi likh rha.... learn to write pseudo code to catch issues before implementing approach.. bc


rotation(_input)
