"""
CP1404/CP5632 Practical
Store email and name in a dictionary
"""

YES = ["YES", "Y", ""]
NO = ["NO", "N"]

email_to_name = {}
user_email = input("Email: ")
while user_email != "":
    user_name = user_email.split("@")
    user_name = user_name[0]
    user_name = user_name.split(".")
    name = ""
    if len(user_name) > 1:
        user_name = " ".join(user_name)
        name = user_name.title()
    else:
        name = user_name[0].title()
    user_name_isvalid = input(f"Is your name {name}? (Y/n)")
    user_name_isvalid = user_name_isvalid.upper()
    if user_name_isvalid in YES:
        email_to_name[name] = user_email
    elif user_name_isvalid in NO:
        user_name = input("Name: ")
        email_to_name[name] = user_email
    user_email = input("Email: ")
