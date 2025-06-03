x_horse = int(input())
y_horse = int(input())
n = int(input())
m = int(input())

x1, y1 = x_horse - 2, y_horse + 1
x2, y2 = x_horse - 1, y_horse + 2
x3, y3 = x_horse + 1, y_horse + 2
x4, y4 = x_horse + 2, y_horse + 1
x5, y5 = x_horse + 2, y_horse - 1
x6, y6 = x_horse + 1, y_horse - 2
x7, y7 = x_horse - 1, y_horse - 2
x8, y8 = x_horse - 2, y_horse - 1

path = 0

for i in range(0,n+1):
    for j in range(0,m+1):
        if (i == x1 and j == y1) or (i == x2 and j == y2) or (i == x3 and j == y3) or (i == x4 and j == y4) or (i == x5 and j == y5) or (i == x6 and j == y6) or (i == x7 and j == y7) or (i == x8 and j == y8):
            break
        else:
            path += 1

print(path)