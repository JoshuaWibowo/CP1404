def main():
    """main function"""
    input_file = open("temps_input.txt", "r")
    for line in input_file:
        print(line)
    input_file.close()


def celsius_to_fahrenheit(fahrenheit_input):
    """Convert celsius to fahrenheit"""
    celsius_output = 5 / 9 * (fahrenheit_input - 32)
    return celsius_output


def fahrenheit_to_celsius(celsius_input):
    """Convert fahrenheit to celsius"""
    fahrenheit_output = celsius_input * 9.0 / 5 + 32
    return fahrenheit_output


main()
