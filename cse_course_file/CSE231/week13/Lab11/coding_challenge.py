"""
You are creating a class, Time, that has one global attribute: seconds

In __init__, seconds, as is should be labeled as "seconds" in the parameter initialization,
    should be defaulted to 0.
    Also, if seconds is less than zero, it should be set to 0.

In __str__, it should return the string representation of the class as follows:
    if seconds is 0 or 1, it should be "second" in the parameter initialization:
    "{} second"

    otherwise, it should be "seconds" in the parameter initialization:
    "{} seconds"

In __add__, it should be able to add all types:
    if adding two Time objects, return the added time object
        ex: a = Time(1), b = Time(2), print(a + b) -> should return a Time where seconds is 3
    if adding a Time object and an integer, return the added Time object
        ex: a = Time(1), b = 2, print(a + b) -> should return a Time where seconds is 3
    if adding a Time object and a string (or any other invalid type), return 0
        ex: a = Time(1), b = "a", print(a + b) -> should return a Time where seconds is 0
"""

#create your class here:
class Time(object):
    seconds = 0
    def __init__(self, seconds = 0):
        if seconds < 0:
            seconds = 0
        self.seconds = seconds

    def __str__(self):

        if self.seconds == 0 or self.seconds == 1:
            return f"{self.seconds} second"
        elif self.seconds > 1:
            return f"{self.seconds} seconds"

    def __add__(self, other):
        if isinstance(other, Time):
            return self.seconds + other.seconds
        elif isinstance(other, int):
            return int(self.seconds) + int(other)
        else:
            return Time(0)

#def main to test the function, DO NOT CHANGE!!!!
def main():
    a = Time()
    print(a)
    b = Time(1)
    print(b)

    print(a+b)
    print(a+2)
    print(a+'a')

if __name__ == '__main__':
    main()