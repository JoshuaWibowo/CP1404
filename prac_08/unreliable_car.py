"""
CP1404/CP5632 Practical
Unreliable car class
"""
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but add reliability variable."""
        distance_driven = super().drive(distance)
        return distance_driven
