"""
1 - 10 pts (Control)

Write a program to check for user input, assume int or float, and ask as follows
"Input a number: {}"

If the number is a "proper fraction" (-1 < number < 1   and the number is NON-ZERO), print "{} is a proper fraction."

If the number falls out of the range, print "{} is not a proper fraction."
"""

"""
Test Cases
Input a number: 0.5
0.5 is a proper fraction.
Input a number: 1.5
1.5 is not a proper fraction.
Input a number: -0.5
-0.5 is a proper fraction.
Input a number: 1
1.0 is not a proper fraction.
Input a number: -1
-1.0 is not a proper fraction.
Input a number: 0
0.0 is not a proper fraction.
"""

num = float(input("Input a number:"))

if (num >-1 and num <1 and num !=0):
    print(str(num) + " is a proper fraction.")
else:
    print(str(num) + " is not a proper fraction.")



