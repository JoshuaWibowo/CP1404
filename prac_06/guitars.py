"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
from prac_06.guitar import Guitar


def main():
    """Demo codes to use car class."""
    guitars = []
    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = input("Cost: ")
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)


main()
