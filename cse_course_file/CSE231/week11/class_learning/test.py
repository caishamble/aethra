

import copy
import math
import cmath

class Force():

    def __init__(self, magnitude=0, angle=0):

        self.magnitude = magnitude
        self.angle = angle

    def get_magnitude(self):

        return self.magnitude

    def get_angle(self):

        return self.angle



    def get_components(self):
        vector = cmath.rect(self.magnitude, math.radians(self.angle))
        return vector.real, vector.imag

    def __str__(self):

        return f"Magnitude: {self.magnitude:.2f}\nAngle: {self.angle:.2f}"

    def __eq__(self, other):

        if not isinstance(other, Force):
            raise RuntimeError("\nBoth objects must be of the Force class")
        return self.magnitude == other.magnitude and self.angle == other.angle

    def __add__(self, other):
        if not isinstance(other, Force):
            raise RuntimeError("\nBoth objects must be of the Force class")

        # Convert both forces to complex numbers
        force1 = cmath.rect(self.magnitude, math.radians(self.angle))
        force2 = cmath.rect(other.magnitude, math.radians(other.angle))

        # Sum the complex forces
        result_force = force1 + force2

        # Calculate magnitude and angle of the result
        magnitude = abs(result_force)
        angle = math.degrees(cmath.phase(result_force))
        if angle < 0:
            angle += 360

        return Force(magnitude, angle)


class ForceCalculator(object):

    def __init__(self, forces=None):

        if forces is None:
            self.forces = {}
        else:
            self.forces = forces

    def get_forces(self):

        return self.forces

    def __getitem__(self, name):

        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        return self.forces[name]

    def add_force(self, name, magnitude, angle):

        if name in self.forces:
            raise RuntimeError(f"\nForce object {name} already exists!")
        self.forces[name] = Force(magnitude, angle)

    def remove_force(self, name):

        if name not in self.forces:
            raise RuntimeError(f"\nForce object {name} does not exist!")
        del self.forces[name]

    def compute_net_force(self):

        net_force = Force()
        for force in self.forces.values():
            net_force += force
        return net_force

    def __str__(self):
        return "\n".join(
            [f"\nForce #{i:02d}: {name}\n{force}" for i, (name, force) in enumerate(self.forces.items(), start=1)])

