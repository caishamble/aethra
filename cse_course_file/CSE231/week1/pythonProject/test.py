n = int(input())

for i in range(1, n+1):
    s = input()
    a = int(s[0])
    b = int(s[2])
    g = int(s[4])
    k = int(s[6])

p = input()
x = int(p[0])
y = int(p[2])

for i in range(1, n+1):
    if (x >= a and x <= a+g) and (y >= b and y <= b+k):
        mark = i
    else:
        mark = -1

print(mark)