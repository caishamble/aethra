"""
Create a program that takes a csv file, of which each line has the following format:
    "Name" (a string), "Year" (an integer),
    "Value1" (an integer, sometimes in the form of "123"),
    and "Value2" (a float, sometimes in the form of "123.456")

and prints out a list of tuples, with each tuple containing the values of each line in the csv file
(except for Value1 and Value2: only the integer/float itself should be included, in other words, no quotation marks).

The first line will be the header, and should be skipped.

When printing out the list of tuples, the program should print out the order of the tuples based on the "name" value, in alphabetical order.
"""

from operator import itemgetter

def read_card_data(fp):
    next(fp,None)
    final_list = []
    for line in fp:
        new_line = []

        line = line.strip().split(',')
        cnt = 0
        for words in line:
            cnt += 1
            if words[0] == '"':
                s = len(words)
                new_words = words[3:s-3]
            else:
                new_words = words
            if cnt == 1 or cnt ==2:
                new_line.append(new_words)
            elif cnt ==3:
                new_line.append(int(new_words))
            else:
                new_line.append(float(new_words))
        final_list.append(tuple(new_line))
    sorted_final_list = sorted(final_list, key = itemgetter(0))
    print(sorted_final_list)
file = open("chall_04.csv", "r", encoding="utf8")

print(read_card_data(file))