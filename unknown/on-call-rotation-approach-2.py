'''

on call rotation of the people is given, 

name, start time, end time

I, 1, 10
J, 5, 7
K, 6, 12
L, 15, 17

Output: needs to be only printed not stored anywhere

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
    changes = []
    for name, start, end in _input:
        changes.append((start, name))
        changes.append((end, name))

    changes.sort()

    on_call = set()

    prev_time = changes[0][0]

    for time, name in changes:
        if time > prev_time and on_call:
            print(prev_time, time, on_call)
        if name in on_call:
            on_call.remove(name)
        else:
            on_call.add(name)
        prev_time = time
        

rotation(_input)

