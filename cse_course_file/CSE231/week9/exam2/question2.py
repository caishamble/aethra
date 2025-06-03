"""
2.      (50 pts, 5 for 1st function, 25 for hidden 1st function, 5 for 2nd function, 15 for hidden 2nd function)
functions to make are read_file() and calculate_eff()

read_file()

Take a file pointer, which is from a csv, and create an overall dictionary with the name as the key,
and the value as a list of the values from the csv file.
(e.g. {'John': [1, 2, 3, 4, 5], 'Jane': [6, 7, 8, 9, 10]}
    if the csv file was: John 1 2 3 4 5 (on one line), (and this on the next line) Jane 6 7 8 9 10)
Skip the first line of course. The values should be the type that they started in (meaning if you typecast,
code would be right, but you should not have to if done correctly)

calculate_eff()

Take the dictionary from read_file() and calculate the efficiency of each person.
Efficiency is defined by the following formula:
    ((GP + NR + PTS) - ((NA - FTA) + (FTN - POT))) / (TO)
Return a dictionary with the name as the key, and the efficiency as the value.
The value should be a float rounded to two decimal places.
(e.g. {'John': 13.23, 'Jane': 2.34}  for some CSV file)

main function to test the functions

def main():
    file = open('file.csv', 'r')
    print(read_file(file))
    print(calculate_eff(read_file(file)))
    file.close()
"""
# def read_file(fp):
#     next(fp,None)
#     name_list = []
#     all_num_list = []
#     for line in fp:
#         line = line.strip().split(',')
#         name_list.append(line[0])
#         all_num_list.append([int(line[x]) for x in range(1,len(line))])
#     my_dict = dict(zip(name_list,all_num_list))
#
#     return my_dict

def read_file(fp):
    next(fp, None)
    dict = {}
    for line in fp:
        line = line.strip("\n").split(",")
        dict[line[0]] = [int(x) for x in range(1,len(line))]

    return dict


def calculate_eff(my_dict):
    new_name_list = []
    new_value_list = []

    for key in my_dict.keys():

        new_name_list.append(key)

        num_list = my_dict[key]
        result = (num_list[3] + num_list[4] + num_list[5] - (num_list[1] - num_list[2]) + (num_list[6] - num_list[7])) / (num_list[0])
        round_result = round(result,2)

        new_value_list.append(round_result)

    new_dict = dict(zip(new_name_list,new_value_list))

    return new_dict


def main():
    file = open('file.csv', 'r')
    file_dict = read_file(file)
    print(file_dict)
    print(calculate_eff(file_dict))

main()