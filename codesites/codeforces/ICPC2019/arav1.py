
number = int(input())


'''
matrix = [[0]*number]*number


matrix[x][y] = 1
print(matrix)

'''
x = 0
y = int(number/2)

data = [[None]*number for _ in range(number)]

data[x][y] = 1
x = x-1
y = y-1

for po in range(2, (number*number)+1):
    if x < 0 and y < 0:
        x = 1
        y = 0
    elif x < 0:
        x = number-1
    elif y < 0:
        y = number-1
    elif data[x][y] is not None:
        x = x+2
        y = y+1
    
    data[x][y] = po
    print(po, x, y)
    y = y-1
    x = x-1
    print(data)

print(data[0])
print(data[1])
print(data[2])