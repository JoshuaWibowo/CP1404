"""
CP1404/CP5632 Practical
Taxi simulator
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Main function."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    menu = "q)uit, c)hoose taxi, d)rive"
    current_taxi = None

    print("Let's drive!")
    print(menu)
    user_input = input(">>> ").lower()
    while user_input != "q":
        if user_input == "c":
            print("ok")

        elif user_input == "d":
            print("ok")

        else:
            print("Invalid choice")

        print(menu)
        user_input = input(">>> ").lower()


main()
