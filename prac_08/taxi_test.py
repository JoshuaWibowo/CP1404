"""CP1404/CP5632 Practical - Client code to use the Taxi class."""

from prac_08.taxi import Taxi


def main():
    """Demo test code to show how to use taxi class."""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)

main()
