
# https://www.hackerrank.com/challenges/2d-array/problem

# Complete the hourglassSum function below.
def hourglassSum(arr):
    row_len = len(arr[0])
    col_len = len(arr)
    print(row_len, col_len)
    max1 = -(sys.maxsize)
    for col in range(row_len-2):
        for row in range(col_len-2):
            sum1 = 0
            sum1 += (arr[row][col]+arr[row][col+1]+arr[row][col+2])
            sum1 += (arr[row+1][col+1])
            sum1 += (arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2])
            print(sum1)
            if max1 < sum1:
                max1 = sum1
    return max1

