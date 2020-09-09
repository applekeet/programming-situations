T = int(input())

def transpose(mat, side):
    for i in range(1, side):
        for j in range(0, i):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
    return mat

def print_matrix(mat):
    for i in mat:
        print(i)
    return 0

def formula_matrix(n):
    mat = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(((i-1)*N) + j)
        mat.append(row)
    return mat

for _ in range(T):
    N = int(input())
    F = formula_matrix(N)
    M = []
    for _ in range(N):
        arr = list(map(int, input().rstrip().split()))
        M.append(arr)
    # arr.sort(reverse = True)
    # print_matrix(M)
    # print("#######")
    ops = 0
    for qq in range(N-1, -1, -1):
        for ee in range(N-1, -1, -1):
            # print(M[qq][ee], F[qq][ee], qq, ee)
            if M[qq][ee] != F[qq][ee]:
                M = transpose(M, qq+1)
                ops += 1
                break
    #print_matrix(M)
    print(ops)
    
    