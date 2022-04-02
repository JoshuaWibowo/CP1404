"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When entering an alphabet, float or any other type than an integer
2. When will a ZeroDivisionError occur?
When entering a zero as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by adding a while loop to make sure that the denominator is not 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
