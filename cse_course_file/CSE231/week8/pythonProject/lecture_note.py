#week 8 dictions and sets

# map data structure
# map data structure is a collection of key-value pairs, where each key is unique, and each key is associated with a value
# map data structure is also known as dictionary in python

# creating a dictionary
my_dict = dict()
type(my_dict) # dict

my_dict = {}
type(my_dict) # dict

teaching_dict = {'sands':19, 'michael': 20, 'john': 21}
print(teaching_dict) # {'sands': 19, 'michael': 20, 'john': 21}

flu_dct = {1918:1e4, 1957:2e6, 1968:1e6, 2009:2e9}
print(flu_dct) # {1918: 10000.0, 1957: 2000000.0, 1968: 1000000.0, 2009: 2000000000.0}

animal_list = ['cat', 'dog', 'elephant', 'giraffe']
animal_dict = {animal_list[x]:0 for x in range(len(animal_list))}
print(animal_dict) # {'cat': 0, 'dog': 0, 'elephant': 0, 'giraffe': 0}

# look up a value in a dictionary

# input the key and get the value
print(teaching_dict['sands']) # 19
print(flu_dct[1918]) # 10000.0
print(animal_dict['cat']) # 0
print(animal_dict['alligator']) # KeyError: 'alligator'
# remember to use key to look up the value in a dictionary, but value to look up the key

print(teaching_dict(18)) # TypeError: 'dict' object is not callable

for teacher in teaching_dict:
    if teaching_dict[teacher] == 18:
        print(teacher) # sands

# add a key-value pair to a dictionary
teaching_dict['xiangbo'] = 19
print(teaching_dict) # {'sands': 19, 'michael': 20, 'john': 21, 'xiangbo': 19} #add in the end


# example add and delete a key-value pair to a dictionary

my_dict = {}
print(my_dict) # {}

# add
my_dict['a'] = 1
print(my_dict) # {'a': 1}

my_dict['b'] = 2
print(my_dict) # {'a': 1, 'b': 2}
my_dict['c'] = 3
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}

# change value of a key
my_dict['a'] = 100
print(my_dict) # {'a': 100, 'b': 2, 'c': 3}

# delete a key-value pair
del my_dict['b']
print(my_dict) # {'a': 100, 'c': 3}


# common way to operate a dictionary

from string import ascii_lowercase
print(ascii_lowercase) # abcdefghijklmnopqrstuvwxyz

ltr_dict = {ltr:0 for ltr in ascii_lowercase}
print(ltr_dict)
# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

sentence = 'my name is xiangbo, i learn electrical engineering'
for ltr in sentence:
    if ltr == ' ' or ltr == ',':
        continue
    ltr_dict[ltr] += 1
print(ltr_dict)

# {'a': 4, 'b': 1, 'c': 2, 'd': 0, 'e': 7, 'f': 0, 'g': 3, 'h': 0, 'i': 6, 'j': 0, 'k': 0, 'l': 3, 'm': 2, 'n': 6, 'o': 1, 'p': 0, 'q': 0, 'r': 3, 's': 1, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 1, 'y': 1, 'z': 0}

for letter in ltr_dict:
    print(letter, end=' ')
# a b c d e f g h i j k l m n o p q r s t u v w x y z

for letter in ltr_dict.keys():
    if ltr_dict[letter] > 0:
        print(letter, end=' ')
# a b c e g i l m n o r s t x y

for letter_count in ltr_dict.values():
    print(letter_count, end=' ')
# 4 1 2 0 7 0 3 0 6 0 0 3 2 6 1 0 0 3 1 1 0 0 0 1 1 0

for letter, letter_count in ltr_dict.items():
    print(letter,'-',letter_count, end=' ')
# a - 4 b - 1 c - 2 d - 0 e - 7 f - 0 g - 3 h - 0 i - 6 j - 0 k - 0 l - 3 m - 2 n - 6 o - 1 p - 0 q - 0 r - 3 s - 1 t - 1 u - 0 v - 0 w - 0 x - 1 y - 1 z - 0


total = 0
for v in ltr_dict.values():
    total += v
    print(f"There were total {total} letters in the sentence")
# There were total 42 letters in the sentence

for k in ltr_dict.keys():
    if ltr_dict[k] > 1:
        print(k, end=' ')
# a c e g i l m n r

for k,v in ltr_dict.items():
    if v == 2:
        print(k, end=' ')
# c m

# dictionary search example

ltr_dict = {ltr:0 for ltr in ascii_lowercase}
sentence = 'my name is xiangbo, i learn electrical engineering'
for ltr in sentence:
    if ltr == ' ' or ltr == ',':
        continue
    ltr_dict[ltr] += 1

del ltr_dict['x']
del ltr_dict['y']

search_key = input('Enter a letter to search: ')
while search_key != 'quit':
    if search_key in ltr_dict:
        print(f"{search_key} appears {ltr_dict[search_key]} times")
    else:
        print(f"{search_key} is not in the dictionary")
    search_key = input('Enter a letter to search: ')

# Enter a letter to search: a # a appears 4 times
# Enter a letter to search: b # b appears 1 times
# Enter a letter to search: c # c appears 2 times
# Enter a letter to search: d # d is not in the dictionary
# Enter a letter to search: quit

# the zip method
animal_list = ['cat', 'dog', 'elephant', 'giraffe']
animal_age_list = [2, 3, 4, 5]
animal_dict = dict(zip(animal_list, animal_age_list))
print(animal_dict) # {'cat': 2, 'dog': 3, 'elephant': 4, 'giraffe': 5}


# sets

my_set = set()
type(my_set) # set

my_set = {}
type(my_set) # dict

my_set = {1, 2, 3, 4, 5}
type(my_set) # set

# update a set
a_set = {1,}
a_set.add(2)
print(a_set) # {1, 2}

a_set.clear()
print(a_set) # set()

for i in range(2,11,2):
    a_set.add(i)
print(a_set) # {2, 4, 6, 8, 10}

a_set.remove(4)
print(a_set) # {2, 6, 8, 10}

if 5 in a_set:
    a_set.remove(5)
print(a_set) # {2, 6, 8, 10}

a_set.discard(6)
print(a_set) # {2, 8, 10}

a_set.discard(5)
print(a_set) # {2, 8, 10}

b_set = a_set.copy()
print(b_set) # {2, 8, 10}


# set operations
a_set = {1, 2, 3, 4, 5}
b_set = {3, 4, 5, 6, 7}

intersection_set = a_set & b_set # {3, 4, 5}
union_set = a_set | b_set # {1, 2, 3, 4, 5, 6, 7}
difference_set = a_set - b_set # {1, 2}
symmetric_difference_set = a_set ^ b_set # {1, 2, 6, 7}

# set operations example
a_set = {1,2,3}
b_set = {3,4,5}
a_set < b_set # False
a_set <= b_set # False
a_set > b_set # False
a_set >= b_set # False
# to compare two sets, it is just to determine if one set is a subset of another set, or a set is a superset of another set

#perfect chapter exercise 1

result_dict = {}

while True:
    user_input_name = input("\nName: ")
    user_input_number = input("\nNumber: ")

    result_dict[user_input_name] = user_input_number

    user_judge = input('\nMore data (y/n)? ')
    if user_judge == 'n':
        break
    else:
        continue


# the way we how to sorted the dictionary
sorted_dict = sorted(result_dict.items(), key=lambda x: x[0])

print("\nThe sorted data:", sorted_dict)