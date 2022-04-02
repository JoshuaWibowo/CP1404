"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def fahrenheit_to_celsius(celsius_input):
    fahrenheit_output = celsius_input * 9.0 / 5 + 32
    return fahrenheit_output


def celsius_to_fahrenheit(fahrenheit_input):
    celsius_output = 5 / 9 * (fahrenheit_input - 32)
    return celsius_output


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = fahrenheit_to_celsius(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = celsius_to_fahrenheit(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
