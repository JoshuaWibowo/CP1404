import shutil
import os


def main():
    """Program to sort files."""
    extensions = []
    # Change to desired directory
    os.chdir(os.getcwd() + '/FilesToSort/')
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        for index, char in enumerate(filename):
            if char == ".":
                extensions.append(filename[index + 1:])

    extensions = set(extensions)

    for extension in extensions:
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass



main()
