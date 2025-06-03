# week 3 STRING in python

s1 = 'spartan'
type(s1)   # the type of s1 is str
s2 = "spartan"
type(s2)   # the type of s2 is str

str(10)
# convert 10 to a string
# '10'

# Recall: UTF8 table convertion in python
x = ord('$')
print(x) # 36

y = chr(36)
print(y) # $

# ord() and chr() are inverse of each other

s1 = 'First\nSecond'
print(s1) # First and Second are on different lines

s2 = 'First\tSecond'
print(s2) # First and Second are separated by a tab

s3 = 'First\\Second'
print(s3) # First\Second

s4 = '\u03c1=1/\u03c3'
print(s4) # ρ=1/σ

s5 = 'This is my first time to use python with \'subtitle\' and this is taught by Dr. Li\' assistant'
print(s5) # This is my first time to use python with 'subtitle' and this is taught by Dr. Li' assistant
# if you want use ' in a string, you need to use \'

s6 = 'C:\\\\Documents\\myfile.txt'
print(s6) # C:\\Documents\myfile.txt


# string as a sequence of characters
s1 = 'Dr. Cai'
print(s1[0]) # D
print(s1[3]) # .
print(s1[4]) # space

print(s1[10]) # IndexError: string index out of range

print(s1[-1]) # i
print(s1[-2]) # a
print(s1[-3]) # C

s2 = input("Enter any word: ")
print(s2[len(s2)-1]) # print the last character of the string

s3 = 'hello'
for x in s3:
    print(x,end=' ') # h e l l o

for i in range(len(s3)):
    print(s3[i],end=' ') # h e l l o

for i in range(0,len(s3),1):
    print(s3[i],end=' ') # h e l l o

for i in range(len(s3)-1,-1,-1):
    print(s3[i],end=' ') # o l l e h

t1 = 'truck'
t2 = t1[0]+t1[1]+'i'+t1[3]+t1[4]
print(t1,t2) # truck trick


# string slicing
s1 = 'Dr. Cai, I am so happy to learn python from you!'
print(s1[0:4]) # Dr.
print(s1[4:8]) #  Cai
print(s1[9:11]) # I

print(s1[12:]) # am so happy to learn python from you!
print(s1[:11]) # Dr. Cai, I
print(s1[:]) # Dr. Cai, I am so happy to learn python from you!

print(s1[::2]) # D. i,Im ohyt er o lra yhn o!
print(s1[1::2]) # r ai  ph o e u!rnpto r u

print(s1[-6:]) # you!
print(s1[-6::-1]) # uoy morf nohtyp nrael ot yppah os ma I ,iaC .rD


# string operators
s1 = 'hi '
s2 = 'mom!'
s3 = s1 + s2
print(s3) # hi mom!

amt = 4
print('I have $',4) # I have $ 4
print('I have $',4,sep='') # I have $4
print('I have $',4,sep=' ') # I have $ 4
print('I have $'+str(amt)) # I have $4


s3 = 'hello'
print(s3*3) # hellohellohello
print(s3*0) # ''
print(s3*-1) # ''
print(s3*-2) # ''
print(s3*-3) # ''
print(s3+'!') # hello!
print(s3+' '+s3) # hello hello
print(s3+str(2)) # hello2

print('I owe you $'+str(25)+' dollars') # I owe you $25 dollars

for i in range(5):
    print('Yo!'*i) # print Yo! 0 times, 1 times, 2 times, 3 times, 4 times

# string comparison
'aa' < 'ab' # True
'Aa' < 'aa' # True
'aa' < 'aA' # False

'cai' in 'xiangbo cai' # True
'chen' in 'xiangbo cai' # False

s1 = 'rubber baby buggy bumpers'
for x in s1:
    if x in 'bg':
        pass
    else:
        print(x,end='') #ruer ay uy umpers



# string methods
s1 = 'dog'
s1.upper()
print(s1) # dog // because s1.upper() is not assigned to s1

s1 = s1.upper()
print(s1) # DOG

dir(s1) # show all the methods of s1

s2 = 'ShOuT'
s3 = s2.lower()
print(s2,s3) # ShOuT shout

s1 = 'where is waldo?'
s1.find('waldo') # 9
s1.find('xiangbo') # -1
s1.index('waldo') # 9
s1.index('xiangbo') # ValueError: substring not found

s1 = '%'
s2 = 'a'
print(s1.isalpha(),s2.isalpha()) # False True


s1 = '   Today is a good    day!      '
len(s1) # 32
s1.strip() # 'Today is a good    day!'
len(s1.strip()) # 23

s1 = 'Here is a COMpliCated String and ChAiN that you need find'
print(s1.lower().find('chain')) # 32

print('my name is {} and I have ${} in my wallet'.format('xiangbo','100'))
# my name is xiangbo and I have $100 in my wallet

print(f"my name is {'xiangbo'} and I have ${'100'} in my wallet")
# my name is xiangbo and I have $100 in my wallet

name = input('Enter your name: ')
amount = float(input('Enter the amount of money you have: '))
print(f"my name is {name} and I have ${amount:.2f} in my wallet")

x = 235.7
s1 = f"{x:@>+10.3f}"
print(s1) #@@+235.700


# string function
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.whitespace)

# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#                                   // whitespace
