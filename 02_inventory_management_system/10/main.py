def execute(input):
    twos = 0
    threes = 0
    
    for line in input:
        m = {}
        for leter in line.strip():
            if leter in m:
                m[leter] += 1
            else:
                m[leter] = 1

        values = m.values()
        if 2 in values:
            twos += 1
        if 3 in values:
            threes += 1

    print twos * threes

f = open("./02_inventory_management_system/10/input.txt", "r")
input = f.readlines()
f.close()

execute(input)