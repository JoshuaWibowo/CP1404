total_number = 5
numbers = []
for number in range(total_number):
    number_input = int(input("Number: "))
    numbers.append(number_input)

first_num, last_num = numbers[0], numbers[-1]
smallest_num, largest_num = min(numbers), max(numbers)
average_num = sum(numbers)/len(numbers)

print(f"The first number is {first_num}")
print(f"The last number is {last_num}")
print(f"The smallest number is {smallest_num}")
print(f"The largest number is {largest_num}")
print(f"The average of the numbers is {average_num}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Enter your username: ")
if user_name in usernames:
    result = "Access granted"
else:
    result = "Access denied"
print(result)
