"""
The challenge:

Create a class, Piano, and the __init__ and __str__ methods.

The Piano class should contain the following attributes:
- brand (a string)
- num_keys (an integer)
- is_playing (a boolean)

By default, the brand should be "Steinway", the num_keys should be 88, and is_playing should be false.

The __str__ method should return a string that says:
"The [brand] piano has [num_keys] keys and is [playing or not playing]."

ex: "The Steinway piano has 88 keys and is not playing." - if is_playing is False
"""

# code the Piano class here
class Piano(object):
    def __init__(self, brand = 'Steinway', num_keys = 88, is_playing = False):
        self.brand = brand
        self.num_keys = num_keys
        self.is_playing = is_playing

    def __str__(self):
        if self.is_playing == True:
            return f"The {self.brand} piano has {self.num_keys} keys and is playing."
        else:
            return f"The {self.brand} piano has {self.num_keys} keys and is not playing."


def main():
    # - Uncomment when you're ready to test your Piano class.

    my_piano1 = Piano()
    print(my_piano1)
    my_piano2 = Piano("Yamaha", 76, True)
    print(my_piano2)
    my_piano3 = Piano("Baldwin", 61, False)
    print(my_piano3)
    my_piano4 = Piano(is_playing = True)
    print(my_piano4)


if __name__ == "__main__":
    main()