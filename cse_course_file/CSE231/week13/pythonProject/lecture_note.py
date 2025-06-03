# scope

# The truth about the namespace(local, global, built-in)

k,v = 0, 0
for k,v in globals().items():
    print(k, v)
# output:
# __name__ __main__
# __doc__ None
# __package__ None
# __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x000002277DE3BB60>
# __spec__ None
# __annotations__ {}
# __builtins__ <module 'builtins' (built-in)>
# __file__ C:\CSE_231\week13\pythonProject\test.py
# __cached__ None
# k __cached__
# v __cached__


# qualified name and unqualified name
import math

# qualified name
print(math.pi)
print(math.sqrt(2))

# unqualified name
pi = 3.14
print(pi)


# LEGB search (local, enclosed, global, built-in)


# example by chatGPT

x = 'global'  # global variable


def outer():
    x = 'enclosing'  # enclosing variable

    def inner():
        x = 'local'  # local variable
        print(x)

    inner()
    print(x)


outer()
print(x)


# output:
# local
# enclosing
# global



# global and local

x = 10  # Global variable

def foo(a, b, c):
    if a > b:
        x = 2  # Local variable, does not affect the global x
    else:
        x = 1  # Local variable, does not affect the global x
    print("---local----")
    for k, v in locals().items():  # Print local variables
        print(k, v)
    return c ** x

y = foo(10, 4, 3)
print("---global----")
for k, v in dict(globals()).items():  # Create a copy of the globals dictionary
    print(k, v)


# output:

# an exmaple to show the built-in scope

# ---local----
# a 10
# b 4
# c 3
# x 2
# ---global----
# __name__ __main__
# __doc__ None
# __package__ None
# __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x0000013869F0BB60>
# __spec__ None
# __annotations__ {}
# __builtins__ <module 'builtins' (built-in)>
# __file__ C:\CSE_231\week13\pythonProject\test.py
# __cached__ None
# x 10
# foo <function foo at 0x000001386A0F3240>
# y 9


# built-in scope

i = 0
for k, v in __builtins__.__dict__.items():
    if i <= 0:
        break
    print(k, v)
    i -= 1



# enclosed scope
x = 3
def foo(b):
    x = 2
    def goo(a):
        return a ** x
    return goo(b)

foo(3) # Output: 9










# local assignment
joe = 1
def kev():
    joe = joe + 1
    return joe
kev() # Output: UnboundLocalError: local variable 'joe' referenced before assignment

# fix code:

joe = 1
def kev():
    global joe
    joe = joe + 1
    return joe
kev() # Output: 2

# the class stuff

#ex1
class A:
    x = 10

    def __init__(self, a):
        self.x = a
    def __str__(self):
        return f"{x},{self.x}"

a_instance = A(20)
print(a_instance) #no output

#ex2
x = 2
class A:
    x = 10

    def __init__(self, a):
        self.x = a
    def __str__(self):
        return f"{x},{self.x}"

a_instance = A(20)
print(a_instance) # Output: 2,20

#ex3
x = 2
class A:
    x = 10

    def __init__(self, a):
        self.x = a
    def __str__(self):
        return f"{A.x},{self.x}"

a_instance = A(20)
print(a_instance) # Output: 10,20