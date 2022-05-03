"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
from prac_06.guitar import Guitar


def main():
    """Demo test code to show how to use Guitar class."""
    guitar_one = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_two = Guitar("Another Guitar", 2013, 16035.40)

    print(f"{guitar_one.name} get_age() - Expected 100. Got {guitar_one.get_age()}")
    print(f"{guitar_two.name} get_age() - Expected 9. Got {guitar_two.get_age()}")
    print(f"{guitar_one.name} is_vintage() - Expected True. Got {guitar_one.is_vintage()}")
    print(f"{guitar_two.name} is_vintage() - Expected False. Got {guitar_two.is_vintage()}")


main()
