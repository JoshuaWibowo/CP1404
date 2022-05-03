"""CP1404/CP5632 Practical - Client code to use the Guitar class."""
from prac_06.guitar import Guitar


def main():
    """Demo codes to use car class."""
    guitars = []
    print("My guitars!")
    # guitar_name = input("Name: ")
    # while guitar_name != "":
    #     guitar_year = int(input("Year: "))
    #     guitar_cost = int(input("Cost: "))
    #     guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    #     guitars.append(guitar)
    #     print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")
    #     print()
    #     guitar_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print()
    print("... \033[3msnip\033[0m ...")
    print()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        response = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i +1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:>10,.2f}{response}")


main()
