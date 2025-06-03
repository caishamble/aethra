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
    pass

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
def read_file(fp):
    pass

def calculate_eff(stats):
    pass

"""
3.      (40pts, 5 for visible, 35 for hidden)
function to make is use_supplies()

Take 4 dictionaries in, 
    supplies, effects, player, items
        supplies is a dictionary with the name as the key, and the value as the amount of supplies found
            (e.g. {'wood': 14, 'scraps': 10, 'metal': 0})
        effects is a dictionary with the name as the key, and the value as a tuple with the player stat type and the effect
            (e.g. {'chocolate': ('health', 2), 'ice cream': ('health', -15), 'metal': ('ammo', 5)})
        player is a dictionary with the player stat type as the key, and the value as the current amount of that stat
            (e.g. {'health': 5, 'water': 3, 'ammo': 10})
        items is a dictionary with the name as the key, and the value as the effect of the item
            (e.g. {'chocolate': 2, 'ice cream': -15, 'metal': 5})
    
    use_supplies will do a series of comparisons to see if, given the dicts, the supply is in items.
        If it is, it will add to the value of it in supplies.
        If it is not, it will add the item to supplies with a value of 1.
    Then, it will check if the item is in effects.
        If it is, it will add the effect to the player stat type in player.
        If it is not, it will do nothing.
    
    Return NOTHING!!! you should be directly changing the input dictionaries in your code, not creating local ones. 
    That way, the dictionaries can just be called as declared in main() to test function with:
    
    def main():
        supplies = {'wood': 14, 'scraps': 10, 'metal': 0}
        effects = {'chocolate': ('health', 2), 'ice cream': ('health', -15), 'metal': ('ammo', 5)}
        player = {'health': 5, 'water': 3, 'ammo': 10}
        items = {'chocolate': 2, 'ice cream': -15, 'metal': 5}
        use_supplies(supplies, effects, player, items)
        print(supplies) # Should print {'wood': 14, 'scraps': 10, 'metal': 1, 'chocolate': 1}
        print(player) # Should print {'health': 7, 'water': 3, 'ammo': 15}
        print(use_supplies(supplies, effects, player, items)) # Should print None
"""
def use_supplies(supplies, effects, player, items):
    pass