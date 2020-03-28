# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K, L):
    # write your code in Python 3.6
    totalNum = len(A)
    if totalNum < (K+L):
        return -1

    finalSum = 0
    for i in range(K):
        finalSum += A[i]

    currentSum = finalSum
    lastChangePosition = 0
    for j in range(K, totalNum):
        currentSum += (A[j] - A[j-K])
        if finalSum < currentSum:
            finalSum = currentSum
            lastChangePosition = j


    ## Alice apples in finalSum
    for i in range(K):
        A[lastChangePosition - i] = 0

    print(A)

    finalSum2 = 0
    for i in range(L):
        finalSum2 += A[i]

    currentSum2 = finalSum2
    for j in range(L, totalNum):
        currentSum2 += (A[j] - A[j-L])
        if finalSum2 < currentSum2:
            finalSum2 = currentSum2

    print(finalSum2)

    return finalSum


print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))
