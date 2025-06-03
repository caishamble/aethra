# week 5 working with files

# opening and closing files objects

fn = 'amanda_gorman.txt'
fp = open(fn, 'r')
type(fp) # file object
fp.close()

# absolute path and relative path

# absolute path
fn = ":C:\\Users\\Owner\\Documents\\Python\\Python-Programming-Projects\\week5\\amanda_gorman.txt"
fp = open(fn, 'r')
fp.close()

# relative path
fn = '\\amanda_gorman.txt'
fp = open(fn, 'r')
fp.close()

# file modes
# r - read
# w - write
# a - append
# r+ - read and write
# w+ - write and read
# a+ - append and read
# b - binary mode
# t - text mode
# x - create
# + - read and write
# U - universal newline

# reading from a file
fn = 'amanda_gorman.txt'
fp = open(fn, 'r')
for line in fp:
    print(line,end='/')
fp.close()
# when you open the file, each line front will add a '/'

fn = 'amanda_gorman.txt'
fp = open(fn, 'r')
for line in fp:
    print(line.strip(),end='/')
fp.close()
# when you open the file, used the strip() method to remove the white space, so the '\n' become '/'

fn = 'amanda_gorman.txt'
fp = open(fn, 'r')
fp.readline()
fp.readline()
for line in fp:
    print(line.strip(),end='/')
fp.close()
# the same as last one, but the first two lines are not printed

fn = 'public_health\\Provisional_COVID-19_Death_Counts_by_Week_Ending_Date_and_State.csv'
fp = open(fn, 'r')
print(fp.readline().strip())

count = 0
for line in fp:
    print(line.strip())
    count += 1
    if count == 10:
        break

# other way to read files

# read the whole file
fn = 'amanda_gorman.txt'
fp = open(fn, 'r')
the_whole = fp.read()
print(the_whole) # print the whole file
print(type(the_whole)) # <class 'str'>
print(len(the_whole)) # the length of the file
fp.close()


# read the whole file as a list of lines
fn = 'poems\\phillis_wheatley.txt'
fp = open(fn, 'r')
the_whole = fp.readlines()     # read the whole file as a list of lines
print(the_whole) # print the whole file
print(type(the_whole)) # <class 'list'>
print(len(the_whole)) # return the number of lines in the file
for line in the_whole:
    print(line.strip())
fp.close()



# writing to a file
fn = 'amanda_gorman.txt'
fp = open(fn, 'w')
poem_line = input('Enter a line of the poem: , or enter quit to stop: ')
while poem_line != 'quit':
    print(poem_line, file=fp)
    poem_line = input('Enter a line of the poem: , or enter quit to stop: ')
fp.close()  # this situation will keep in seperate lines


fn = 'amanda_gorman.txt'
fp = open(fn, 'w')
poem_line = input('Enter a line of the poem: , or enter quit to stop: ')
while poem_line != 'quit':
    fp.write(poem_line + '\n')
    poem_line = input('Enter a line of the poem: , or enter quit to stop: ')
fp.close()             # this situation is keep all write lines in the file if u write fp.write(poem_line)



# what if you forget to close the file?
with open('amanda_gorman.txt', 'r') as fp:
    for line in fp:
        if line[0].lower == 't':
            print(line.strip())
        print('Done')
# this will not need to write fp.close() at the end, it will automatically close the file after the block of code is executed















# common run time errors
# FileNotFoundError
# FileExistsError
# ValueError
# TypeError
# IndexError
# KeyError
# NameError
# ZeroDivisionError
# SyntaxError
# AssertionError
# EOFError

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
try:
    if a/b > 1:
        print('a is greater than b')
    elif a/b == 1:
        print('a is equal to b')
    else:
        print('a is less than b')
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid input')


fn = input('Enter the name of the file: ')
try:
    fp = open(fn, 'r')
    for line in fp:
        print(line.strip())
except FileNotFoundError:
    print('File not found')
else:
    fp.close()
finally:
    print('Done')


# write test for your code

def foo(a,b,c):
    if a + b < b - c:
        return a + b
    return a * b

try:
    assert foo(1,2,3) == 3
    assert foo(3,2,1) == 6
    assert foo(1,3,2) == 3
    print('All tests passed')
except AssertionError:
    print('Test failed')


def my_func(a,b):
    if a + b > 10:
        raise ArithmeticError
    return a + b
try:
    x = int(input('Enter a number: '))
    y = my_func(x,5)
except ValueError:
    print('Invalid input')
except ArithmeticError:
    print("You went over. Too bad!")
print('Done')
