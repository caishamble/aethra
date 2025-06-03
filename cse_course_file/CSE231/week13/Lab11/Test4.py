import unittest
from lab11 import Vector

class Tests8(unittest.TestCase):
    """
    Begin magnitude Tests
    """

    def test_magnitude(self):
        print("V1 = Vector(1,2)")
        v1 = Vector(1, 2)
        result1 = v1.magnitude()
        print("Instructor V1 magnitude: ", 2.24)
        print("Student V1 magnitude: ", result1)
        assert result1 == 2.24

        print('-' * 20)
        print("V2= Vector(2,3)")
        v2 = Vector(2, 3)
        result2 = v2.magnitude()
        print("Instructor V2 magnitude: ", 3.61)
        print("Student V2 magnitude: ", result2)
        assert result2 == 3.61


class Tests9(unittest.TestCase):
    """
    Begin unit Tests
    """

    def test_unit1(self):
        print("V1 = Vector(1,2)")
        v1 = Vector(1, 2)
        result1 = v1.unit()
        print("Instructor unit V1: ", "(0.45, 0.89)")
        print("Student unit V1: ", str(v1))
        assert str(v1) == "(0.45, 0.89)" and result1 == None

        print('-' * 20)
        print("V2= Vector(2,3)")
        v2 = Vector(2, 3)
        result2 = v2.unit()
        print("Instructor unit V2 : ", "(0.55, 0.83)")
        print("Student unit V2: ", str(v2))
        assert str(v2) == "(0.55, 0.83)" and result2 == None

    def test_unit2(self):
        print('-' * 20)
        print("zero= Vector()")
        zero = Vector()
        try:
            result2 = zero.unit()
        except ValueError as e:
            assert str(e) == "Cannot convert zero vector to a unit vector"


if __name__ == "__main__":
    unittest.main()
