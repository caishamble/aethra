# week 6 list and tuple

# list is a mutable, iterable, sequence and collection of items

# create a list
my_lst = list()
type(my_lst) # list

my_lst = list("Spartans")
print(my_lst) # ['S', 'p', 'a', 'r', 't', 'a', 'n', 's']

my_lst = []
type(my_lst) # list

my_lst = list[1, 2, 3, 4, 5]
print(my_lst) # [1, 2, 3, 4, 5]

my_lst = [x for x in range(1,20,2)]
print(my_lst) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

my_lst = [x**2 for x in range(1,20,2)]
print(my_lst) # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

yr_lst = [1 for x in range(10)]
print(yr_lst) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

yr_lst = ['a' for x in range(10)]
print(yr_lst) # ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']


# index and slicing list
my_lst = [1, 2, 3, 4, 5]

print(my_lst[0]) # 1
print(my_lst[1]) # 2
print(my_lst[2]) # 3

print(my_lst[-1])# 5
print(my_lst[-2])# 4

my_lst[2] = 100
print(my_lst) # [1, 2, 100, 4, 5]
my_lst[3] += 2
print(my_lst) # [1, 2, 100, 6, 5]

# slicing

a_sub_lst = my_lst[1:3]
print(a_sub_lst) # [2, 100]

a_sub_lst = my_lst[:3]
print(a_sub_lst) # [1, 2, 100]

a_sub_lst = my_lst[3:]
print(a_sub_lst) # [6, 5]

a_sub_lst = my_lst[1:7:2]
print(a_sub_lst) # [2, 6]

a_sub_lst = my_lst[1:11]
print(a_sub_lst) # [2, 100, 6, 5]

a_sub_lst = my_lst[::-1]
print(a_sub_lst) # [5, 6, 100, 2, 1]


# list operations
a_lst = [1, 2, 3, 4, 5]
b_lst = [6, 7, 8, 9, 10]

c_lst = a_lst + b_lst
print(c_lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d_lst = a_lst[1:3]+b_lst[3:]
print(d_lst) # [2, 3, 9, 10]

e_lst = a_lst*3
print(e_lst) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

f_lst = a_lst + [7]
print(f_lst) # [1, 2, 3, 4, 5, 7]

g_lst = a_lst[1] + b_lst
print(g_lst) # wrong, for this to work, a_lst[1] should be a list



# list iteration

employees_lst = ['John', 'Doe', 'Jane', 'Doe', 'Tom', 'Jerry']
for employee in employees_lst:
    print(employee,end=' ')
# John Doe Jane Doe Tom Jerry

purchase_lst = [100, 200, 300, 400, 500]
total = 0
for purchase in purchase_lst:
    total += purchase
print(total) # 1500

min_purchase = purchase_lst[0]
for purchase in purchase_lst:
    if purchase < min_purchase:
        min_purchase = purchase
print(min_purchase) # 100

num_lst = [1, 2, 3, 4, 5]
for num in num_lst:
    num *= 0.9
print(num_lst) # [1, 2, 3, 4, 5]
# didn't work, num is a copy of the list element, not the element itself

# method 1
for i in range(len(num_lst)):
    num_lst[i] *= 0.9
print(num_lst) # [0.9, 1.8, 2.7, 3.6, 4.5]

# method 2
i = 0
for p in num_lst:
    num_lst[i] *= 0.9
    i += 1
print(num_lst) # [0.9, 1.8, 2.7, 3.6, 4.5]


for i,num in enumerate(num_lst):
    print(i,num)
# 0 0.9
# 1 1.8
# 2 2.7
# 3 3.6
# 4 4.5
# enumerate returns a tuple of index and element


# list function
from random import randint
my_lst = [randint(0,10) + 1 for x in range(12)]
print(my_lst) # [4, 5, 3, 6, 5, 6, 7, 2, 8, 8, 9, 5]

len(my_lst) # 12
max(my_lst) # 9
min(my_lst) # 2
sum(my_lst) # 68
sorted(my_lst) # [2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9]
sorted(my_lst, reverse=True) # [9, 8, 8, 7, 6, 6, 5, 5, 5, 4, 3, 2]
sorted(my_lst, reverse=True)[0] # 9



# list methods
my_lst = [1, 2, 3, 4, 5]

my_lst.append(6)
print(my_lst) # [1, 2, 3, 4, 5, 6]

my_lst.insert(3, 100)
# my_lst.insert(index, value)  change the value of list at the index position to the value
print(my_lst) # [1, 2, 3, 100, 4, 5, 6]

my_lst.insert(1000000,100)
# if the index is greater than the length of the list, the value is appended to the end of the list
print(my_lst) # [1, 2, 3, 100, 4, 5, 6, 100]


my_lst.remove(100)
print(my_lst) # [1, 2, 3, 4, 5, 6]

my_lst.pop()
# pop removes the last element of the list
print(my_lst) # [1, 2, 3, 4, 5]

my_lst.pop(2)
print(my_lst) # [1, 2, 4, 5]

my_lst.clear()
print(my_lst) # []

my_lst = [1, 2, 3, 4, 5]

my_lst.index(3) # 2

my_lst.count(3) # 1: the number of 3 in the list

my_lst.reverse()
print(my_lst) # [5, 4, 3, 2, 1]

my_lst.sort()
print(my_lst) # [1, 2, 3, 4, 5]

s1 = 'a,b,c,d,e,f,g'
s1_lst = s1.split(',')
print(s1_lst) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

s2 = ' '.join(s1_lst)
print(s2) # a b c d e f g


# nested list
student_data = [['luck',90,97,92],['jane',89,90,92],['john',90,92,94]]

print(student_data[0]) # ['luck', 90, 97, 92]
print(student_data[0][0]) # luck
print(student_data[0][1]) # 90
print(student_data[0][2]) # 97
print(student_data[2][3]) # 94

for student in student_data:
    for data in student:
        print(data, end=' ')
    print()
# luck 90 97 92
# jane 89 90 92
# john 90 92 94

# reference and copy
a_lst = [1, 2, 3, 4, 5]
b_lst = a_lst
b_lst[2] = 100
print(a_lst) # [1, 2, 100, 4, 5]
# a_lst and b_lst are the same list, changing one changes the other, the data store in the same list

a_lst = [1, 2, 3, 4, 5]
b_lst = a_lst[:]
b_lst[2] = 100
print(a_lst) # [1, 2, 3, 4, 5]
# a_lst and b_lst are different list, changing one doesn't change the other, the data store in different list



a_lst = [1, 2, 3, 4, 5]
b_lst = a_lst
if a_lst is b_lst:
    print('same')
else:
    print('different')
# same

a_lst = [1, 2, 3, 4, 5]
b_lst = a_lst[:]    # b_lst = a_lst.copy()
if a_lst is b_lst:
    print('same')
else:
    print('different')
# different



# now the very hard mode

sub_lst = [1,2,3]
weird_lst = ['a','b',sub_lst]
copy_lst = weird_lst[:]
copy_lst[2][1] = 100
print(weird_lst) # ['a', 'b', [1, 100, 3]]
print(copy_lst) # ['a', 'b', [1, 100, 3]]
# the sub list is the same for both lists, changing one changes the other

from copy import deepcopy
sub_lst = [1,2,3]
weird_lst = ['a','b',sub_lst]
copy_lst = deepcopy(weird_lst)
copy_lst[2][1] = 100
print(weird_lst) # ['a', 'b', [1, 2, 3]]
print(copy_lst) # ['a', 'b', [1, 100, 3]]
# deepcopy creates a new list and copies the elements of the original list to the new list
# the sub list is different for both lists, changing one doesn't change the other

# tuple
# tuple is an immutable, iterable, sequence and collection of items
# difference between list and tuple is that list is mutable and tuple is immutable

my_tup = tuple(1, 2, 3, 4, 5)
type(my_tup) # tuple

print(my_tup[2]) # 3

new_tup = tuple(my_lst)
print(new_tup) # (1, 2, 3, 4, 5)

new_lst = list(new_tup)
print(new_lst) # [1, 2, 3, 4, 5]


# revisiting function return using tuple
def f(a,b,c):
    d = a**b
    e = b**c
    return d,e
result = f(2,3,4)
type(result) # tuple
print(result[0]) # 8


# list comprehension
a_lst = [1, 2, 3, 4, 5]
b_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a_lst > b_lst) # False
print(a_lst < b_lst) # True
print(a_lst == b_lst) # False

# two dementional list sort

student_data = [['luck',90,97,92],['jane',89,90,92],['john',90,92,94]]

sorted_data = sorted(student_data)
print(sorted_data)
# according to the first element of each list
# [['jane', 89, 90, 92], ['john', 90, 92, 94], ['luck', 90, 97, 92]]

# if you want to print in different row
for student in sorted_data:
    print(student)

from operator import itemgetter
sorted_data = sorted(student_data, key=itemgetter(3))
print(sorted_data)
# according to the fourth element of each list
# [['jane', 89, 90, 92], ['luck', 90, 97, 92], ['john', 90, 92, 94]]

sorted_data = sorted(student_data, key=itemgetter(1,2,3))
print(sorted_data)
# according to the first, second and third element of each list
# [['jane', 89, 90, 92], ['john', 90, 92, 94], ['luck', 90, 97, 92]]

