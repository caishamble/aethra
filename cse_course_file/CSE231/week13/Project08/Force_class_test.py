import unittest
from enze_force import Force


class ForceTest(unittest.TestCase):

    def test_init_get_methods(self):

        # Create zero Force object
        F1 = Force()
        self.assertEqual((F1.get_magnitude(), F1.get_angle()), (0, 0))

        # Create custom force
        magnitude = 3.567
        angle = 210
        F2 = Force(magnitude, angle)
        self.assertEqual((F2.get_magnitude(), F2.get_angle()), (magnitude, angle))

        # Create custom force to test get_components
        magnitude = 10
        angle = 135
        F3 = Force(magnitude, angle)
        x_comp, y_comp = F3.get_components()
        self.assertEqual((round(x_comp, 2), round(y_comp, 2)), (-7.07, 7.07))


    def test_str_eq_add_methods(self):

        F1 = Force()
        F2 = Force(25, 315)
        F3 = Force(50, 18)

        # __str__ method test
        self.assertEqual(str(F1), "Magnitude: 0.00\nAngle: 0.00")
        self.assertEqual(str(F2), "Magnitude: 25.00\nAngle: 315.00")
        self.assertEqual(str(F3), "Magnitude: 50.00\nAngle: 18.00")

        # __eq__ method test
        self.assertEqual(F2, F2)
        self.assertNotEqual(F1, F2)

        #__add__ method test
        sum1 = (F1+F2)

        self.assertEqual(sum1, F2)

        sum2 = F2+F3
        self.assertEqual((round(sum2.get_magnitude(), 2), round(sum2.get_angle(), 2)), (65.27, 358.04))

if __name__ == '__main__':
    unittest.main()