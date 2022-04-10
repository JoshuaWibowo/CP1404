"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects_data = []
    for line in input_file:
        part = line.strip().split(',')
        part[-1] = int(part[-1])
        subjects_data.append(part)
    input_file.close()
    return subjects_data


main()
