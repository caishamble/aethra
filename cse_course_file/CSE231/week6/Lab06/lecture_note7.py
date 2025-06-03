# week 7 more details about functions

# scope

# local scope and global scope
def f(x):
    total = 0
    for i in range(x):
        total *= i
    x = 1
    return
x = 10
y = f(x)
print(x,y) # 10, None
# print(total) # error becoz total is local to the function f

# arguments, parameters and reference
def f(a_str, b_lst, c_int):
    c_int += 10
    b_lst[0] = 7
    a_str += 'Sands'
    print("in function:", a_str, b_lst, c_int) # Dr. Sands [7, 2, 3, 4, 5] 12
    return

a = 'Dr. '
b = [1,2,3,4,5]
c = 2
f(a,b,c)
print("outside function:", a,b,c) # Dr. [7, 2, 3, 4, 5] 2

d = b
d[1] = 10
print(d,b) # [7, 10, 3, 4, 5] [7, 10, 3, 4, 5]

print(id(b),id(d)) # 140270736439872 140270736439872  same
print(id(c)) # 140270736439872

def f(a,b,c):
    a = a * b
    b = b +c
    c = a /b
    return a,b,c
my_tup = f(10,2,3)
for i, x in enumerate(my_tup):
    print(i,x) # 0 20 1 5 2 4.0


# default values and parameters
def f(a = 'MSU', b = 0):
    return (a[b])

print(f('Spartan',5)) # a
print(f()) # M
print(f('python')) # P
print(f(5)) # type erro, because 5 is not a string (default value of a is string)
print(f(b=1)) # S

def f (a, b = 10):
    return a + b
print(f(3)) # 13
print(f(3,2)) # 5
print(f(b=3)) # error, because a is not given
print(f(a=3)) # 13


# problem
def f(a_lst = [0,0,0], b = 0):
    a_lst[b] = 10
    return a_lst
print(f()) # [10, 0, 0]
print(f(b=2)) # [10, 0, 10]  not[0, 0, 10] because a_lst is not reinitialized


# describing function

# annotation
def count_words(s:str) -> int:
    return len(s.split())

count_words('hello world') # 2

# docstring
def count_words(s:str) -> int:
    """Return the number of words in s."""
    return len(s.split())