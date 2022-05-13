"""CP1404/CP5632 Practical - Client code to use the Taxi class."""

from prac_08.taxi import Taxi


def main():
    """Demo test code to show how to use taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()