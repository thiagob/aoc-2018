def execute(data):
    polymer = list(data.strip())

    idx = 0
    while (idx + 1) < len(polymer):
        if polymer[idx].lower() == polymer[idx + 1].lower() and polymer[idx] != polymer[idx + 1]:
            del polymer[idx + 1]
            del polymer[idx]
            idx -= 1
            if idx < 0:
                idx = 0
        else:
            idx += 1

    print len(polymer)

f = open("./05_alchemical_reduction/input.txt", "r")
data = f.read()
f.close()

execute(data)
