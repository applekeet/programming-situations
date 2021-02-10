import string

def solution(x):
    a = string.ascii_lowercase
    r_a = a[::-1]
    y = x.maketrans(a, r_a)
    # print(y, a, r_a)
    z = x.translate(y)
    
    return z
            

print(solution("kzws ov kzws ov armwztr yzm qzbvtr"))
