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
    user_email = input("Email: ")
