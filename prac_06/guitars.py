"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
from prac_06.guitar import Guitar


def main():
    """Demo codes to use car class."""
    guitars = []
    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = int(input("Cost: "))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")
        print()
        guitar_name = input("Name: ")
    print()
    print("... \033[3msnip ...")
    print()


main()
