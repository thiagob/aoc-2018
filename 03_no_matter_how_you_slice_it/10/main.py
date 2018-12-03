import re

def execute(input):
    size = 1500
    fabric = [[0 for x in range(size)] for y in range(size)]
    conflicts = 0

    for line in input:
        parts = re.findall('\d+', line)

        claim = {
            "id": int(parts[0]),
            "col": int(parts[1]),
            "row": int(parts[2]),
            "width": int(parts[3]),
            "height": int(parts[4])
        }

        for r in range(claim["row"], claim["row"] + claim["height"]):
            for c in range(claim["col"], claim["col"] + claim["width"]):
                if fabric[r][c] == 0:
                    fabric[r][c] = claim["id"]
                elif fabric[r][c] != "X":
                    fabric[r][c] = "X"
                    conflicts += 1

    print conflicts

f = open("./03_no_matter_how_you_slice_it/10/input.txt", "r")
input = f.readlines()
f.close()

execute(input)
