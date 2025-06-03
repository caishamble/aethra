"""
1.      (30 pts, 5 for visible, 25 for hidden)
function to make is max_occurences()

Take any list of anything, and return the item that occurs the most times in the list.
if there is a tie, return the alphabetically/numerically first item that has the most occurences.
(e.g. Orange and Kiwi are the items tied for max occurnces, Kiwi should be reported, as it is alphabetically first)
(e.g. 1 and 2 are the items tied for max occurnces, 1 should be reported, as it is numerically first)

main function to test the function

def main():
    print(max_occurences([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 1, 2, 3, 1, 2])) # 1
    print(max_occurences(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'b'])) # a
    print(max_occurences(['a', 'b', 'c', 'd', 'e', 'b', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd])) # a
    print(max_occurences(['orange', 'kiwi', 'apple', 'banana', 'kiwi', 'orange', 'plum'])) # kiwi
"""

def max_occurences(lst):
    cnt_list = []
    sample_list = []
    max_mark = -1
    for element in lst:
        if element not in sample_list:
            sample_list.append(element)
            cnt_list.append(int(1))
        elif element in sample_list:
            index = sample_list.index(element)
            cnt_list[index] += 1
    for count in cnt_list:
        if count > max_mark:
            max_mark = count
    my_dict = dict(zip(sample_list,cnt_list))
    new_list = []
    for key,value in my_dict.items():
        if value == max_mark:
            new_list.append(key)
    sorted_new_list = sorted(new_list)
    return sorted_new_list[0]

def main():
    print(max_occurences([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 1, 2, 3, 1, 2])) # 1
    print(max_occurences(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'b'])) # a
    print(max_occurences(['a', 'b', 'c', 'd', 'e', 'b', 'g', 'h', 'i', 'j', 'a', 'c', 'd'])) # a
    print(max_occurences(['orange', 'kiwi', 'apple', 'banana', 'kiwi', 'orange', 'plum'])) # kiwi

main()