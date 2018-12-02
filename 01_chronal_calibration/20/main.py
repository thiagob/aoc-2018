def execute(input):
    frequencies = {}
    frequency = 0
    i = -1

    while True:
        i += 1
        if len(input) <= i:
            i = 0

        frequencies[frequency] = 1

        change = int(input[i])
        frequency += change

        if frequency in frequencies:
            print frequency
            break


f = open("./01_chronal_calibration/10/input.txt", "r")
input = f.readlines()
f.close()

execute(input)