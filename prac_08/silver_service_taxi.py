"""
CP1404/CP5632 Practical
SilverServiceTaxi  class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    price_per_km = Taxi.price_per_km

    def __init__(self, name, fuel, fanciness):
        """Initialise a  SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.fanciness = fanciness
