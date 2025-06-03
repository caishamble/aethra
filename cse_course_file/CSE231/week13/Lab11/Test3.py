import unittest
from lab11 import Vector


class Tests6(unittest.TestCase):
    """
    Begin __mul__ Tests
    """

    def test_mul(self):
        print("v1 = Vector(1,2)")
        print("a = 2")
        a = 2
        v1 = Vector(1, 2)
        v = v1 * a
        print("Instructor v1*a: ", "(2.00, 4.00)")
        print('Instructor type: Vector')
        print("Student v1*a vector: ", str(v))
        print('Student type: ', type(v))
        assert str(v) == "(2.00, 4.00)" and type(v) == Vector

        print('-' * 20)
        print("v1= Vector(1,2)")
        print("v2= Vector(2,3)")
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        y = v1 * v2
        print("Instructor v1*v2: ", 8.0)
        print("Student v1*v2: ", y)
        assert y == 8.0


class Tests7(unittest.TestCase):
    """
    Begin __rmul__ Tests
    """

    def test_rmul(self):
        print("v1 = Vector(2,3)")
        print("a = 2")
        a = 2
        v1 = Vector(2, 3)
        v = a * v1
        print("Instructor a*v1: ", "(4.00, 6.00)")
        print('Instructor type: Vector')
        print("Student a*v1 vector: ", str(v))
        print('Student type: ', type(v))
        assert str(v) == "(4.00, 6.00)" and type(v) == Vector

        print('-' * 20)
        print("v1= Vector(1,2)")
        print("v2= Vector(2,3)")
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        y = v1 * v2
        print("Instructor v1*v2: ", 8.0)
        print("Student v1*v2: ", y)
        assert y == 8.0


if __name__ == "__main__":
    unittest.main()