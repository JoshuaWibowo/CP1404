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
    user_bill = 0

    print("Let's drive!")
    print(menu)
    user_input = input(">>> ").lower()
    while user_input != "q":
        if user_input == "c":
            for taxi in range(len(taxis)):
                print(f"{taxi} - {taxis[taxi]}")
            user_taxi = int(input("Choose taxi: "))
            if user_taxi not in range(len(taxis)):
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[user_taxi]

        elif user_input == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid choice")

        print(f"Bill to date: ${user_bill:.2f}")
        print(menu)
        user_input = input(">>> ").lower()


main()
