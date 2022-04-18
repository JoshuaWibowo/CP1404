"""
CP1404/CP5632 Practical
Hex colour code finder
"""

CODE_TO_COLOUR = {"Black": "#000000", "OrangeRed1": "#ff4500",
                  "Yellow1": "#ffff00", "Green1": "#00ff00",
                  "Blue1": "#0000ff", "Cyan1": "#00ffff",
                  "Gold1": "#ffd700", "GhostWhite": "#f8f8ff",
                  "Harlequin": "#3fff00", "NeonGreen": "#39ff14"}
for key in CODE_TO_COLOUR:  # print all the colour
    print(f"{key:<10} is {CODE_TO_COLOUR[key]:<}")

colour_name = input("Enter colour name: ").lower()  # user input
colour_key = [key.lower() for key in CODE_TO_COLOUR.keys()]  # create the lower key
lower_to_upper = dict(zip(colour_key, CODE_TO_COLOUR.keys()))  # create new dict of lower and upper key
while colour_name != "":
    if colour_name in colour_key:
        print(f"{lower_to_upper[colour_name]:<10} is {CODE_TO_COLOUR[lower_to_upper[colour_name]]:<}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
