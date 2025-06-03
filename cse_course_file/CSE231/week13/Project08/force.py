###########################################################
# CSE 231 Project 8 - Force Calculator
#
# Class Force:
#     Properties: magnitude (float), angle (float)
#     Methods: __init__(magnitude=0, angle=0), get_magnitude(),
#              get_angle(), get_components(), __str__(), __eq__(other),
#              __add__(other)
#
# Class ForceCalculator:
#     Properties: forces (dict)
#     Methods: __init__(forces=None), get_forces(), __getitem__(name),
#              add_force(name, magnitude, angle), remove_force(name),
#              compute_net_force(), __str__()
###########################################################

import copy
import math


class Force(object):
    """
    A class to represent a force with a magnitude and angle.
    functions:
        - __init__(magnitude=0, angle=0): Initializes a new Force
         object with the given magnitude and angle
        - get_magnitude(): Returns the magnitude of the force
        - get_angle(): Returns the angle of the force in degrees
        - get_components(): Calculates and returns the x and y
        components of the force
        - __str__(): Returns a string representation of the force
        - __eq__(other): Checks if two Force objects are equal
        - __add__(other): Adds two Force objects together to
        get the resultant force
    """
    def __init__(self, magnitude=0, angle=0):
        """
        Initializes a Force object with a given magnitude and angle.

        Parameters:
        - magnitude (float, optional): The magnitude of the
        force (default is 0).
        - angle (float, optional): The angle of the force in
        degrees (default is 0).
        """
        self.magnitude = magnitude
        self.angle = angle

    def get_magnitude(self):
        """
        Returns the magnitude of the force.

        Returns:
        - float: The magnitude of the force.
        """
        return self.magnitude

    def get_angle(self):
        """
        Returns the angle of the force in degrees.

        Returns:
        - float: The angle of the force in degrees.
        """
        return self.angle

    def get_components(self):
        """
        Calculates and returns the x and y components of the force.

        Returns:
        - tuple (float, float): The x and y components of the force.
        """

        # Calculate the x and y components of the force
        x_comp = self.magnitude * math.cos(math.radians(self.angle))
        y_comp = self.magnitude * math.sin(math.radians(self.angle))
        return x_comp, y_comp

    def __str__(self):
        """
        Returns a string representation of the force.

        Returns:
        - str: A string representation of the force.
        """
        return f"Magnitude: {self.magnitude:.2f}\nAngle: {self.angle:.2f}"

    def __eq__(self, other):
        """
        Checks if two Force objects are equal.

        Parameters:
        - other (Force): Another Force object to compare with.

        Returns:
        - bool: True if the forces are equal, False otherwise.
        """
        if not isinstance(other, Force):
            raise RuntimeError("\nBoth objects must be of the Force class")
        return self.magnitude == other.magnitude and self.angle == other.angle

    def __add__(self, other):
        """
        Adds two Force objects together to get the resultant force.

        Parameters:
        - other (Force): Another Force object to add.

        Returns:
        - Force: The resultant force.
        """
        if not isinstance(other, Force):
            raise RuntimeError("\nBoth objects must be of the Force class")
        # Calculate the x and y components of the two forces
        x_first, y_first = self.get_components()
        x_second, y_second = other.get_components()

        # Calculate the x and y components of the resultant force
        x_sum = x_first + x_second
        y_sum = y_first + y_second

        # Calculate the magnitude and angle of the resultant force
        degree = math.degrees(math.atan2(y_sum, x_sum))
        if degree < 0:
            degree += 360
        return Force(math.sqrt(x_sum ** 2 + y_sum ** 2), degree)


class ForceCalculator(object):
    """
    A class to represent a calculator of forces.
    functions:
        - __init__(forces=None): Initializes a new ForceCalculator
        object with the given forces
        - get_forces(): Returns the dictionary of forces in the calculator
        - __getitem__(name): Gets a force from the calculator by name
        - add_force(name, magnitude, angle): Adds a new force to the
        calculator
        - remove_force(name): Removes a force from the calculator
        - compute_net_force(): Computes the net force from all forces
         in the calculator
        - __str__(): Returns a string representation of all forces in the
         calculator

    """
    def __init__(self, forces=None):
        """
        Initializes a ForceCalculator object with a dictionary of forces.

        Parameters:
        - forces (dict, optional): A dictionary of Force objects
        (default is None).
        """
        if forces is None:
            self.forces = {}
        else:
            self.forces = forces

    def get_forces(self):
        """
        Returns the dictionary of forces in the calculator.

        Returns:
        - dict: The dictionary of forces.
        """
        return self.forces

    def __getitem__(self, name):
        """
        Gets a force from the calculator by name.

        Parameters:
        - name (str): The name of the force to retrieve.

        Returns:
        - Force: The force object.
        """

        # Get the force from the calculator
        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        return self.forces[name]

    def add_force(self, name, magnitude, angle):
        """
        Adds a new force to the calculator.

        Parameters:
        - name (str): The name of the new force.
        - magnitude (float): The magnitude of the new force.
        - angle (float): The angle of the new force in degrees.
        """

        # Add the force to the calculator
        if name in self.forces:
            raise RuntimeError(f"\nForce object {name} already exists!")
        self.forces[name] = Force(magnitude, angle)

    def remove_force(self, name):
        """
        Removes a force from the calculator.

        Parameters:
        - name (str): The name of the force to remove.
        """

        # Remove the force from the calculator
        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        del self.forces[name]

    def compute_net_force(self):
        """
        Computes the net force from all forces in the calculator.

        Returns:
        - Force: The net force.
        """

        # Calculate the net force from all forces in the calculator
        net_force = Force()
        for force in self.forces.values():
            net_force += force
        return net_force

    def __str__(self):
        """
        Returns a string representation of all forces in the calculator.

        Returns:
        - str: A string representation of all forces.
        """
        result = ""
        for i, (name, force) in enumerate(self.forces.items(), start=1):
            result += f"\nForce #{i:02d}: {name}\n{str(force)}"
        return result
