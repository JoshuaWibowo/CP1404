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
        category = input(f"What category would you like to sort {extension} files into? ")

        try:
            os.mkdir(category)
        except FileExistsError:
            pass

        for filename in os.listdir('.'):
            # Ignore directories, just process files
            if os.path.isdir(filename):
                continue
            if extension == filename[-(len(extension)):]:
                shutil.move(filename, f'{category}/' + filename)


main()
