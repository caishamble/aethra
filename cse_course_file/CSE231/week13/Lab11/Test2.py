import unittest
from lab11 import Vector


class Tests4(unittest.TestCase):
    """
    Begin __add__ Tests
    """

    def test_add(self):
        print("v1= Vector(1,2)")
        print("v2= Vector(2,3.5)")
        v1 = Vector(1, 2)
        v2 = Vector(2, 3.5)
        v = v1 + v2
        print("Instructor v1+v2: ", "(3.00, 5.50)")
        print('Instructor type: Vector')
        print("Student vector: ", str(v))
        print('Student type: ', type(v))
        assert str(v) == "(3.00, 5.50)" and type(v) == Vector

        print('-' * 20)
        print("v1= Vector(0.5,2.5)")
        print("v2= Vector(1.5,1.5)")
        v1 = Vector(0.5, 2.5)
        v2 = Vector(1.5, 1.5)
        v = v1 + v2
        print("Instructor v1+v2: ", "(2.00, 4.00)")
        print('Instructor type: Vector')
        print("Student vector: ", str(v))
        print('Student type: ', type(v))
        assert str(v) == "(2.00, 4.00)" and type(v) == Vector


class Tests5(unittest.TestCase):
    """
    Begin __sub__ Tests
    """

    def test_sub(self):
        print("v1= Vector(1,2)")
        print("v2= Vector(2,3.5)")
        v1 = Vector(1, 2)
        v2 = Vector(2, 3.5)
        v = v1 - v2
        print("Instructor v1+v2: ", "(-1.00, -1.50)")
        print('Instructor type: Vector')
        print("Student vector: ", str(v))
        print('Student type: ', type(v))
        assert str(v) == "(-1.00, -1.50)" and type(v) == Vector

        print('-' * 20)
        print("v1= Vector(0.5,2.5)")
        print("v2= Vector(1.5,1.5)")
        v1 = Vector(0.5, 2.5)
        v2 = Vector(1.5, 1.5)
        v = v1 - v2
        print("Instructor v1+v2: ", "(-1.00, 1.00)")
        print('Instructor type: Vector')
        print("Student vector: ", str(v))
        print('Student type: ', type(v))
        assert str(v) == "(-1.00, 1.00)" and type(v) == Vector


if __name__ == "__main__":
    unittest.main()