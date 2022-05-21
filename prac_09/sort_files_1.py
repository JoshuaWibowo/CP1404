import shutil
import os


def main():
    """Program to sort files."""
    extension = []
    # Change to desired directory
    os.chdir(os.getcwd() + '/FilesToSort/')
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        for index, char in enumerate(filename):
            if char == ".":
                extension.append(filename[index + 1:])



main()
