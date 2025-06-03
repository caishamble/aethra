import unittest
from enze_force import Force, ForceCalculator


class ForceCalculatorTest(unittest.TestCase):

    def test_init_get_methods(self):

        # Default calculator
        calculator1 = ForceCalculator()
        self.assertEqual(calculator1.get_forces(), {})

        # Initialize calculator with prebuilt force map
        forces = {"f1": Force(83, 60)}
        calculator2 = ForceCalculator(forces)
        self.assertEqual(calculator2.get_forces(), forces)

        # __getitem__ method: valid case
        self.assertEqual(calculator2['f1'], forces['f1'])

        # __getitem__ method: invalid case
        with self.assertRaises(RuntimeError) as e:
            F = calculator2['f2']
        self.assertEqual(str(e.exception), "\nForce object f2 does not exist!")

    def test_add_remove_methods(self):

        # Add force: valid case
        calculator1 = ForceCalculator()
        magnitude, angle = 21, 90
        calculator1.add_force("f1", magnitude, angle)
        self.assertEqual(calculator1.get_forces(), {"f1": Force(magnitude, angle)})

        # Add force: invalid case
        with self.assertRaises(RuntimeError) as e:
            calculator1.add_force("f1", magnitude, angle)
        self.assertEqual(str(e.exception), "\nForce object f1 already exists!")

        # Remove force: valid case
        calculator1.remove_force("f1")
        self.assertEqual(calculator1.get_forces(), {})

        # Remove force: invalid case
        with self.assertRaises(RuntimeError) as e:
            calculator1.remove_force("f1")
        self.assertEqual(str(e.exception), "\nForce object f1 does not exist!")

    def test_compute_force_str(self):

        # Initialize calculator
        forces = {'f1': Force(25, 315), 'f2': Force(50, 18), 'f3': Force(124, 90)}
        calculator1 = ForceCalculator(forces)

        # __str__ method: with force objects
        expected_str = f"\nForce #01: f1\n{str(forces['f1'])}"
        expected_str += f"\nForce #02: f2\n{str(forces['f2'])}"
        expected_str += f"\nForce #03: f3\n{str(forces['f3'])}"

        self.assertEqual(str(calculator1), expected_str)

        # __str__ method: empty
        calculator2 = ForceCalculator()
        self.assertEqual(str(calculator2), "")

        # Compute force: with force objects
        R = calculator1.compute_net_force()
        self.assertEqual((round(R.get_magnitude(), 2), round(R.get_angle(), 2)), (138.14, 61.82))

        # Compute force: empty
        R2 = calculator2.compute_net_force()
        self.assertEqual((round(R2.get_magnitude(), 2), round(R2.get_angle(), 2)), (0, 0))

if __name__ == '__main__':
    unittest.main()