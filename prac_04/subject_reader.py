"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        part = line.strip().split(',')
        part[-1] = int(part[-1])
        subject_data.append(part)
    input_file.close()
    return subject_data


def display_subject(subject_data):
    """Display subject data"""
    for data in subject_data:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students")


main()
