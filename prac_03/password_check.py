"""
Description: Simple password checker
Name: Joshua Timothy Gratio Wibowo
"""
PASS_MIN_LENGTH = 5


def main():
    """Password checker main function"""
    user_password = get_password()

    print_asterisks(user_password)


def print_asterisks(user_password):
    for char in user_password:
        print("*", end='')


def get_password():
    user_password = input(f"Enter {PASS_MIN_LENGTH} char password: ")
    while len(user_password) != PASS_MIN_LENGTH:
        print(f"Invalid password, must be {PASS_MIN_LENGTH} char long")
        user_password = input(f"Enter {PASS_MIN_LENGTH} char password: ")
    return user_password


main()
