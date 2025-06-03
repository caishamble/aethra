# object-oriented programming
# features of OOP
# 1. Encapsulation: wrapping up of data and methods into a single unit
# 2. Inheritance: a class can inherit
# 3. Polymorphism: ability to take multiple forms


# class definition

class Example(object):
    pass
print(type(Example)) # <class 'type'>

my_example = Example()
print(type(my_example)) # <class '__main__.Example'>


# constructor method

class Example(object):
    def __init__(self):
        self.x = 10
        self.y = 20

dir(Example) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


# make an instance of the class


# in a file called dog.py
class Dog(object):
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        if age < 0:
            self.age = 1
        else:
            self.age = age


# in a file called main.py
# import Dog
classic_dog = Dog('Rex', 'German Shepherd',7)
xiangbo_dog = Dog('Xiaohei', 'Golden Retriever', -1)
xiangbo2_dog = Dog('Xiaohei', 'Golden Retriever', 1)

type(classic_dog) # <class '__main__.Dog'>
dir(classic_dog) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'breed', 'name']

# they add agg, breed, name to the object

print(xiangbo_dog.age) # 1
print(xiangbo2_dog.name) # Xiaohei

id(xiangbo_dog) # 140502895218432
id(xiangbo2_dog) # 140502895218368


# class methods
class Dog(object):
    def __init__(self, name, breed, size, age):
        self.name = name
        self.breed = breed
        self.size = size
        self.age = age
    def __str__(self):
        return f"{self.name} is a {self.size} {self.breed} and is {self.age} years old."
    def __repr__(self):
        return "<class Dog>"
    def bark(self,n):
        if self.size == 'big':
            return 'Woof!' * n
        elif self.size == 'medium':
            return 'woof' * n
        else:
            return 'yip' * n

# in a file called main.py
# import Dog
sands_dog = Dog('Sandy', 'Golden Retriever', 'big', 7)
print(sands_dog.bark(3)) # Woof!Woof!Woof!
print(sands_dog) # Sandy is a big Golden Retriever and is 7 years old.

tiny_dog = Dog('Tiny', 'Chihuahua', 'small', 2)
print(tiny_dog.bark(3)) # yipyipyip
print(tiny_dog) # Tiny is a small Chihuahua and is 2 years old.




# class example
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"<class Point>"
    def quadrant(self):
        if self.x > 0:
            if self.y > 0:
                return 'I'
            else:
                return 'IV'
        else:
            if self.y > 0:
                return 'II'
            else:
                return 'III'
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

p1 = Point(3,4)
p2 = Point(-2,1)
print(p1.quadrant()) # I
print(p2.quadrant()) # II
print(p1.distance(p2)) # 5.0
print(p1) # (3,4)


# visibility
# public variables: variables that can be accessed from outside the class
# private variables: variables that can only be accessed from inside the class (can only modify by the class designer)
# protected variables: variables that can only be accessed from inside the class and its subclasses

class HospitalQueue(object):
    def __init__(self):
        self.__queue = []
    def __str__(self):
        return f"There are {len(self.__queue)} patients in the queue."
    def add_patient(self, name, priority):
        i = 0
        while i < len(self.__queue) and self.__queue[i][1] >= priority:
            i += 1
        self.__queue.insert(i, (name, priority))
    def call_next_patient(self):
        next_patient = self.__queue[0]
        self.__queue.pop(0)
        return next_patient

my_q = HospitalQueue()
print(my_q) # There are 0 patients in the queue.

my_q.add_patient('Alice', 5)
print(my_q) # There are 1 patients in the queue.

my_q.add_patient('Bob', 3)
print(my_q) # There are 2 patients in the queue.

next_patient = my_q.call_next_patient()
print(next_patient) # ('Bob', 3)

print(my_q) # There are 1 patients in the queue.


class Account(object):
    __id = 4000123456

    def __init__(self):
        self.id = Account.__id
        Account.__id += 1
        self.__balance = 0

    def __str__(self):
        return f"{self.id}: ${self.__balance:6,.2f}."

    def update_balance(self, amount):
        self.__balance += amount

X = Account()
Y = Account()
Z = Account()

Y.update_balance(100)
Z.update_balance(150)

print(f"{X}\n{Y}\n{Z}")

# 4000123456: $  0.00.
# 4000123457: $100.00.
# 4000123458: $150.00.


class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours % 24
        self.minutes = minutes % 60
        # Adjust hours if minutes are over 59
        self.hours = (self.hours + minutes // 60) % 24

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def add(self, other):
        new_hours = (self.hours + other.hours + (self.minutes + other.minutes) // 60) % 24
        new_minutes = (self.minutes + other.minutes) % 60
        return Clock(new_hours, new_minutes)

# Example usage:
clock1 = Clock(10, 45)
clock2 = Clock(3, 30)
result = clock1.add(clock2)
print(result)  # Output: 14:15



# overloading
class A(object):
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a} {self.b}"


# artithmetic operations
# x + y => x.__add__(y)
# x - y => x.__sub__(y)
# x * y => x.__mul__(y)
# x / y => x.__div__(y)
# x // y => x.__floordiv__(y)
# x % y => x.__mod__(y)
# x ** y => x.__pow__(y)
# x == y => x.__eq__(y)
# x != y => x.__ne__(y)



class Duration(object):
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes."
    def __add__(self, other):
        new_hours = self.hours + other.hours + (self.minutes + other.minutes) // 60
        new_minutes = (self.minutes + other.minutes) % 60
        return Duration(new_hours, new_minutes)
    def __sub__(self, other):
        new_hours = self.hours - other.hours
        new_minutes = self.minutes - other.minutes
        if new_minutes < 0:
            new_hours -= 1
            new_minutes += 60
        return Duration(new_hours, new_minutes)

time1 = Duration(3, 45)
time2 = Duration(2, 30)
print(time1 + time2) # 6 hours and 15 minutes.
print(time1 - time2) # 1 hours and 15 minutes.


# x > y => x.__gt__(y)
# x < y => x.__lt__(y)
# x >= y => x.__ge__(y)
# x <= y => x.__le__(y)
# x == y => x.__eq__(y)
# x != y => x.__ne__(y)

# introspection

class Duration(object):
    def __init__(self, hours, minutes):
        self.hours = hours + minutes // 60
        self.minutes = minutes % 60
    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes."
    def __add__(self, other):
        if type(other) == Duration:
            return Duration(self.hours + other.hours, self.minutes + other.minutes)
        elif type(other) == int:
            return Duration(self.hours + other, self.minutes)
        else:
            return None

time1 = Duration(3, 45)
time2 = Duration(2, 30)
print(time1 + time2) # 6 hours and 15 minutes.
print(time1 + 2) # 5 hours and 45 minutes.
print(time1 + 'hello') # None



# inheritance
class A(object):
    def __init__(self, a):
        self.a = a
    def __str__(self):
        return f"A({self.a})"

a = A(5)
print(a) # A(5)

class B(A):
    def __str__(self):
        return f"B({self.a})"


a = A(3)
b = B(4)
print(a) # A(3)
print(b) # B(4)


# another example

class Animal(object):
    def __init__(self, common_name):
        self.common_name = common_name
    def __str__(self):
        return f"A {self.common_name}."
    def move(self):
        return 'moving'

class Bird(Animal):
    def __init__(self, common_name, can_fly):
        Animal.__init__(self, common_name)
        self.can_fly = can_fly
    def move(self):
        if self.can_fly:
            return 'flying'
        else:
            return Animal.move(self)

tiger = Animal('tiger')
parakeet = Bird('parakeet', True)
ostriech = Bird('ostriech', False)
print(tiger, parakeet, ostriech) # A tiger. A parakeet. A ostriech.

animals_lst = [tiger, parakeet, ostriech, Animal('wolf')]
for animal in animals_lst:
    print(animal.move())
# moving
# flying
# moving
# moving



