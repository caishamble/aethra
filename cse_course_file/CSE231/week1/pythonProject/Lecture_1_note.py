#week 1 class demonstration

MILES_TO_KMS = 1.60934
MILES_TO_LEAGUES = 1 / 3

# Get user input for miles and convert it to a float
miles = input("Please enter your miles to convert: ")
miles_float = float(miles)

# Perform the conversions
kilometers = miles_float * MILES_TO_KMS
leagues = miles_float * MILES_TO_LEAGUES

# Print the results
print(miles, "miles is", round(kilometers,2), "kilometers.")
print(miles, "miles is", round(leagues,2), "leagues.")


# 1. type function

x = 1
type(x)    # int
pi = 3.141592653589793
type(pi)   # float

decimal = 231
binary = 0b11100111
octal = 0o311
hexadecimal = 0xE7
print(decimal, binary, octal, hexadecimal)  #suppose to be all 231


my_name = 'Xiangbo'
type(my_name)  #str

y = None
type(y)    # NoneType

z = print("Xiangbo")
type(z)    # NoneType

bool(1)      # true       any none 0
bool(0)      # false
bool('')     # false
bool('No')   # true

# 2.use of math operation

# for the easy +,-,*,/ I don't mention

x = 11 // 3
print(x)       # ans = 3

y = 11 % 3
print(y)       # ans = 2

e = 3 ** 2
print(e)       # ans = 9


# 3. import modules

import math

x = math.floor(3.79)
y = math.sqrt(64)
z = math.fabs(-25)
k = math.sin(math.pi/6)   # python don't understand 30 degree, but pi/6
z = round(math.sin(math.pi/6),2)
print (x,y,z)



# 4.input and output

print("my name is xiangbo")

my_name = 'Xiangbo'  # equal writing    my_name = "xiangbo"

print(my_name)

# the use of the sep and end

print ("I want to print this into two seperate line","oh yes you are good",sep="\n")

# well here actually you will add "sep into two things you want to print, for a \n will result a new row"
# you can change sep="\n" into sep="balabala", then balabala will appear in two sentence

print ("I want to write this on the same line",end=" ")
print ("I got you")
# auto print in two sentence will result in two row but with the end='' will be in the same
# also if you want still in 2 rows, you can end='\n', or if you want a bigger space, then end='\t' (with a tab in it)


users_input = input("Enter something here")
type(users_input)
# the default of the input() will result in str
# to convert the you can use

users_input = int(input("Enter something here"))
result_1 = users_input +3
print(result_1)
# if you didn't use int in first row, it will result error.



# Sample Demonstration Practice (Convert)

EUROS_PER_DOLLAR = 0.74957

dollars_str = input("Input dollars: ")
dollars_flt = float(dollars_str)

print("Euros:", round(dollars_flt * EUROS_PER_DOLLAR,2))

