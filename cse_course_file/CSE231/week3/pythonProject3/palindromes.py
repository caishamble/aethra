import string

origin_str = "Madam, I'm Adam"
my_str = origin_str.lower()
result_str = ''

# find the good
for letter in my_str:
    if letter in string.ascii_lowercase or letter in string.digits:
        result_str += letter
print(result_str)

# igonre the bad
for letter in my_str:
    if letter in string.whitespace + string.punctuation:
        result_str = result_str.replace(letter, '')
print(result_str)


# check if it is a palindrome

# method 1: index method
front = 0
end = len(result_str) - 1
mid = end / 2

while end >= mid:
    if result_str[front] != result_str[end]:
        print('not a palindrome')
        break
    front += 1
    end -= 1
else:
    print('it is a palindrome')

# method 2: slice method
check_str = my_str
while check_str:
    if check_str[0] != check_str[-1]:
        print('not a palindrome')
        break
    check_str = check_str[1:-1]
else:
    print('it is a palindrome')


# method 3: reverse method
if my_str == my_str[::-1]:
    print('it is a palindrome')
else:
    print('not a palindrome')