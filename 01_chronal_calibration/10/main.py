def execute(input):
    frequency = 0

    for change in input:
        frequency += int(change)

    print frequency


f = open("./01_chronal_calibration/10/input.txt", "r")
input = f.readlines()
f.close()

execute(input)