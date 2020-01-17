def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    
    
    for i in range(days):
        
        states2 = []
        f1 = -1
        f2 = -1
        f3 = -1
        for j in (states):
            f3 = f2
            f2 = f1
            f1 = j
            if f2 != -1:
                if f1 == 0:
                    if f3 == -1 or f3 == 0:
                        states2.append(0)
                    else:
                        states2.append(1)
                if f1 == 1:
                    if f3 == -1 or f3 ==0:
                        states2.append(1)
                    else:
                        states2.append(0)
        
        print(f1, f2, f3)
        if f2 == 0:
            states2.append(0)
        else:
            states2.append(1)
        
        states = states2
            
    while states != []:
        print(states.pop(0), end=" ")


cellCompete([1,0,0,0,0,1,0,0], 1)