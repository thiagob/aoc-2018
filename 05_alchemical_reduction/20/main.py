import string

def reduce_polymer(polymer):
    idx = 0
    polymer = list(polymer)
    while (idx + 1) < len(polymer):
        if polymer[idx].lower() == polymer[idx + 1].lower() and polymer[idx] != polymer[idx + 1]:
            del polymer[idx:idx+2]
            idx -= 1
            if idx < 0:
                idx = 0
        else:
            idx += 1

    return len(polymer)

def execute(data):
    #polymer = list(data.strip())

    shortest = len(data)
    for letter in string.ascii_lowercase:
        polymer = data.replace(letter, '')
        polymer = polymer.replace(letter.upper(), '')

        lenght = reduce_polymer(polymer)
        
        if lenght < shortest:
            shortest = lenght

    print shortest

f = open("./05_alchemical_reduction/input.txt", "r")
data = f.read()
f.close()

execute(data)