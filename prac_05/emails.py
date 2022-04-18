email_to_name = {}
user_email = input("Email: ")
while user_email != "":
    user_name = user_email.split("@")
    user_name = user_name[0]
    user_name = user_name.split(".")
    user_email = input("Email: ")
