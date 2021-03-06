"""
CP1404/CP5632 Practical
Store email and name in a dictionary
"""

YES = ["YES", "Y", ""]
NO = ["NO", "N"]


def main():
    """Main function"""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        name = email_name_separator(user_email)
        email_to_name = name_isvalid(email_to_name, name, user_email)
        user_email = input("Email: ")
    print("")
    for usr_name in email_to_name:
        print(f"{usr_name} ({email_to_name[usr_name]})")


def name_isvalid(email_to_name, name, user_email):
    """Check if username is valid or no"""
    user_name_isvalid = input(f"Is your name {name}? (Y/n) ")
    user_name_isvalid = user_name_isvalid.upper()
    if user_name_isvalid in YES:
        email_to_name[name] = user_email
    elif user_name_isvalid in NO:
        name = input("Name: ")
        email_to_name[name] = user_email
    return email_to_name


def email_name_separator(user_email):
    """Separate name from email"""
    user_name = user_email.split("@")
    user_name = user_name[0]
    user_name = user_name.split(".")
    if len(user_name) > 1:
        user_name = " ".join(user_name)
        name = user_name.title()
    else:
        name = user_name[0].title()
    return name


main()
