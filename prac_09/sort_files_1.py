import shutil
import os


def main():
    """Program to sort files."""
    # Change to desired directory
    os.chdir('FilesToSort')
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue


main()
