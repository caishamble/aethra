"""
In this program, you are required to write code that can convert degree celsius to fahrenheit

Input a fahrenheit temperature and output the celsius equivalent.
Besides, you also need to judge that whether the celsius is hot, cold or moderate.
If the celsius is greater than 25, print "It is hot."
If the celsius is less than 5, print "It is cold."
If the celsius is between 5 and 25, print "It is moderate."(inclusive)
"""

num = int((input("Input a fahrenheit temperature:")))
celsius = (num - 32) * 5.0/9.0
if celsius > 25:
    print(f"{celsius} It is hot.")
elif celsius < 5:
    print(f"{celsius} It is cold.")
else:
    print(f"{celsius} It is moderate.")