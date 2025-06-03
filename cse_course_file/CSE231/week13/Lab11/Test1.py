import unittest
from lab11 import Vector


class Tests1(unittest.TestCase):
    """
    Begin __init__str Tests
    """

    def test_init_and_str(self):
        print("v= Vector()")
        v = Vector()
        print("Instructor vector: ", "(0.00, 0.00)")
        print("Student vector: ", str(v))
        assert str(v) == "(0.00, 0.00)"

        print("-" * 20)
        print("v= Vector(1)")
        v = Vector(1)
        print("Instructor vector: ", "(1.00, 0.00)")
        print("Student vector: ", str(v))
        assert str(v) == "(1.00, 0.00)"

        print("-" * 20)
        print("v= Vector(y=1)")
        v = Vector(y=1)
        print("Instructor vector: ", "(0.00, 1.00)")
        print("Student vector: ", str(v))
        assert str(v) == "(0.00, 1.00)"

        print("-" * 20)
        print("v= Vector(2,3)")
        v = Vector(2, 3)
        print("Instructor vector: ", "(2.00, 3.00)")
        print("Student vector: ", str(v))
        assert str(v) == "(2.00, 3.00)"


class Tests2(unittest.TestCase):
    """
    Begin __repr__ Tests
    """

    def test_repr(self):
        print("v= Vector()")
        v = Vector()
        print("Instructor vector: ", "(0.00, 0.00)")
        print("Student vector: ", v.__repr__())
        assert v.__repr__() == "(0.00, 0.00)"

        print("-" * 20)
        print("v= Vector(2,3)")
        v = Vector(2, 3)
        print("Instructor vector: ", "(2.00, 3.00)")
        print("Student vector: ", str(v))
        assert v.__repr__() == "(2.00, 3.00)"


class Tests3(unittest.TestCase):
    """
    Begin __eql__ Tests
    """

    def test_equal(self):
        print("V1 = Vector(1,2)")
        v1 = Vector(1, 2)
        result1 = v1 == v1
        print("Instructor V1==V1: ", True)
        print("Student V1==V1: ", result1)
        assert result1 == True

        print('-' * 20)
        print("v1= Vector(1,2)")
        print("v2= Vector(2,3)")
        v2 = Vector(2, 3)
        result2 = v1 == v2
        print("Instructor V1==V2: ", False)
        print("Student V1==V2: ", result2)
        assert result2 == False

if __name__ == "__main__":
    unittest.main()
