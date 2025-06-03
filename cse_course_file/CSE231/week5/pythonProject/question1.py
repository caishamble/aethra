def method_func(x,a,b,c):
    if x > 0 :
        return (a * x + b) ** c
    elif x < 0:
        return (a * x - b) ** c
    elif x == 0:
        return c
print(method_func(3,1,24,3))