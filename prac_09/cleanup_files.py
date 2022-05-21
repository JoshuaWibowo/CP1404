import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for index, char in enumerate(filename):
        if char.isupper():
            if index == 0:
                new_name += char
            else:
                if filename[index - 1].islower():
                    new_name += " " + char
        else:
            new_name += char

    new_name = new_name.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
