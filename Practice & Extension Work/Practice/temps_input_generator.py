import random

repeats = 0
input_file = open("temps_input.txt", "w")
# no_of_temps = int(input("How many temp data? "))
no_of_temps = 15
while repeats != no_of_temps:
    temp = float(random.uniform(-200, 200))
    print(temp, file=input_file)
    repeats += 1
input_file.close()
