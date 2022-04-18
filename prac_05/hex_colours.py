"""
CP1404/CP5632 Practical
Hex colour code finder
"""

CODE_TO_COLOUR = {"Black": "#000000", "OrangeRed1": "#ff4500",
                  "Yellow1": "#ffff00", "Green1": "#00ff00",
                  "Blue1": "#0000ff", "Cyan1": "#00ffff",
                  "Gold1": "#ffd700", "GhostWhite": "#f8f8ff",
                  "Harlequin": "#3fff00", "NeonGreen": "#39ff14"}
for key in CODE_TO_COLOUR:
    print(f"{key:<10} is {CODE_TO_COLOUR[key]:<}")

colour_name = input("Enter colour name: ").lower()
colour_key = [key.lower() for key in CODE_TO_COLOUR.keys()]
print(colour_key)

