"""
Description: Simple password checker
Name: Joshua Timothy Gratio Wibowo
"""

PASS_MIN_LENGTH = 5
user_password = input(f"Enter {PASS_MIN_LENGTH} char password: ")

while len(user_password) != PASS_MIN_LENGTH:
    print(f"Invalid password, must be {PASS_MIN_LENGTH} char long")
    user_password = input(f"Enter {PASS_MIN_LENGTH} char password: ")

for char in user_password:
    print("*", end='')
