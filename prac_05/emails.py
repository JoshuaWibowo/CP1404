"""
CP1404/CP5632 Practical
Store email and name in a dictionary
"""

VALID_INPUT = ["Y", "N", "", "YES", "NO"]

email_to_name = {}
user_email = input("Email: ")
while user_email != "":
    user_name = user_email.split("@")
    user_name = user_name[0]
    user_name = user_name.split(".")
    for name in range(len(user_name)):
        user_name[name] = user_name[name].title()
    if len(user_name) > 1:
        user_name = " ".join(user_name)
    user_name_isvalid = input(f"Is your name {user_name}? (Y/n)").upper()
    while user_name_isvalid not in VALID_INPUT:
        print("Invalid input")
        user_name_isvalid = input(f"Is your name {user_name}? (Y/n)").upper()

    email_to_name[user_name] = user_email
    user_email = input("Email: ")
