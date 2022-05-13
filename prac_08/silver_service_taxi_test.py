"""CP1404/CP5632 Practical - Client code to use the SilverServiceTaxi  class."""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to show how to use SilverServiceTaxi class."""
    my_taxi = SilverServiceTaxi("Hummer", 200, 2)
    my_taxi.drive(18)
    print(my_taxi.get_fare())
    print(my_taxi)


main()
