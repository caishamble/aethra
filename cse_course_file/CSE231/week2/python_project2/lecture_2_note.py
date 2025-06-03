#  Boolean type

x = True
type(x)             # bool

y = False
type(y)             # bool

# Relational operators

#    > greater
#    < less
#    >= greater or equal
#    <= less or equal
#    == equal
#    != not equal

"apple" < "bird"
# true, compare the first letter, a<b

"apple" < "asteroid"
# true, compare the seconde letter, p<s

"apple" < "applesauce"
# true, same apple, but no letter after apple, but still have after applesauce

"apple" < "Asteroid"
# false
# reason: In ASCII, the letter 'A'~'Z' is 65 to 90, but 'a'~'z' is 97 to 122

# unicode
x = '10\u00F72'
print (x)    # output: 10 ÷ 2 (00F7 in unicode is symbol '÷')

# the table change in chr and number
print(ord('x')) # output: 120
print(chr(65))  # output: A

# branching statement // in this part, I already know the basic stuff, here is just appendix
x,y,z = 1,2,3
if x<y<z:
    print(x)
print(y,z)
# this is is good on python
x>1 and y>1 # both true then true, otherwise, all false
x>1 or y<1  # only on is true, then all true, false only on both false
# both 2 above is really easy to understand

# example of third way: not

a = 10
if not a > 5:
    a -= 5
print(a)

# example of totaly use

sunny = False
day_off = True
if sunny and day_off:
    print("Beach!")
elif not sunny and day_off:
    print("Video Game!")
else:
    print("School!")
# output: Video Game

# one line way to write

a = int(input("Enter a number: "))
b=(a * 2) if a<10 else (a // 2)
# similar is below
# if a<10:
#    b = a*2
# else:
#    b = a//2
print(a,b)

# the order not > and > or


# repetition
# while loops
a = 10
b = 3
while a>b:
    a -= 1
    print(a,b)
print("Done!")

# use of sentinel
# use sentinel value = -1 to end users input
numbers = []
print("Enter numbers to add to the list. Enter -1 to stop.")
while True:
    number = int(input("Number: "))
    if number == -1:  # Sentinel value
        break
    numbers.append(number)

print("You entered:", numbers)

# in python, if 'continue' ever exist, then will back 'while' sentence

# a template for user_input

user_input = int(input("Enter a positive number less than 100: "))

while user_input < 1 or user_input > 100:
    user_input = int(input("Enter a positive number less than 100: "))

print("Your number is",user_input)

# iteration

name = 'shamble'
for c in name:
    print(c)
print("Done!")      # ouput: s \n h \n  a \n  m \n b \n l\n e\n Done!

# or the other example:


name = 'shamble'
a = 0
for k in name:
    print(' '*a,k)
    a += 1
print('Done!')


# range function
range(1,10,1) # output:1,2,3,...,9
# start integer, end integer, update value
# for the start integer, auto start from 0, for the update value, auto start from 1
range(10) # output: 0,1,2,3,...,9
range(10,1,-1) # output: 10,9,8,...,2 (won't reach 1)

inner = 0
outer = 0
for i in range(5):
    for j in range(4):
        inner += 1
    outer += 1
print(inner,outer)

