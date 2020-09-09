T = int(input())

for _ in range(T):
    N = int(input())
    S = list(map(int, input().rstrip().split()))
    if all(v == 0 for v in S):
        print("1 1")
        exit
    
    P = [] # people
    checklist = {}
    t = 0
    while True: # one loop counts one time unit
        for i in range(N):
            P.append(((i+1)*S[i]) + t)
        print(P)
        for i in P:
            if i in checklist.keys():
                checklist[i] += 1
        print(checklist)
        break
    