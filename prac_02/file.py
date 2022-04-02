# 1.
user_name = input("What is your name? ")
name_file = open("name.txt", "a")
print(user_name, file=name_file)
name_file.close()

# 2.
name_file = open("name.txt", "r")
for name in name_file:
    print(f"Your name is {name}", end='')
name_file.close()

# 3.
numbers_file = open("numbers.txt", "r")
first_number = numbers_file.readline()
second_number = numbers_file.readline()
total = int(first_number[:-1]) + int(second_number[:-1])  # use slicing to remove the \n
print(total)
numbers_file.close()

# 4.
total = 0
numbers_file = open("numbers.txt", "r")
number_list = numbers_file.read().split("\n")
for i in number_list:
    total += int(i)
print(total)
numbers_file.close()
