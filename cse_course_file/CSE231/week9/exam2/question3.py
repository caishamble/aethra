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

    IF ATTRIBUTES IN THE PLAYER REACH 0,
        no negative numbers allowed.

    Return NOTHING!!! you should be directly changing the input dictionaries in your code, not creating local ones.
    That way, the dictionaries can just be called as declared in main() to test function with:

    def main():
        supplies = {'wood': 14, 'scraps': 10, 'metal': 0}
        effects = {'chocolate': ('health', 2), 'ice cream': ('health', -15), 'metal': ('ammo', 5)}
        player = {'health': 5, 'water': 3, 'ammo': 10}
        items = {'chocolate': 2, 'ice cream': 1, 'metal': 5}
        use_supplies(supplies, effects, player, items)
        print(supplies)
        print(player)
        print(use_supplies(supplies, effects, player, items)) # Should print None
"""


def use_supplies(supplies, effects, player, items):
    for item in items.keys():
        if item in supplies.keys():
            supplies[item] -=1

    for item in items.keys():
        if item in effects.keys():

            value1 = effects[item][0]
            value2 = effects[item][1]
            for key_player in player.keys():
                if key_player == value1:
                    player[key_player] += value2
def main():
    supplies = {'wood': 14, 'scraps': 10, 'metal': 0}
    effects = {'chocolate': ('health', 2), 'ice cream': ('health', -15), 'metal': ('ammo', 5)}
    player = {'health': 5, 'water': 3, 'ammo': 10}
    items = {'chocolate': 2, 'ice cream': 1, 'metal': 5}
    use_supplies(supplies, effects, player, items)
    print(supplies)  # Should print {'wood': 14, 'scraps': 10, 'metal': 1, 'chocolate': 1}
    print(player)  # Should print {'health': 7, 'water': 3, 'ammo': 15}
    print(use_supplies(supplies, effects, player, items))  # Should print None

main()