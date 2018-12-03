import re

def execute(input):
    size = 1500
    fabric = [[0 for x in range(size)] for y in range(size)]
    conflicts = 0
    ids = []

    for line in input:
        parts = re.findall('\d+', line)

        claim = {
            "id": int(parts[0]),
            "col": int(parts[1]),
            "row": int(parts[2]),
            "width": int(parts[3]),
            "height": int(parts[4])
        }

        ids.append(claim["id"])

        for r in range(claim["row"], claim["row"] + claim["height"]):
            for c in range(claim["col"], claim["col"] + claim["width"]):
                # OK
                if fabric[r][c] == 0:
                    fabric[r][c] = claim["id"]
                # Conflict
                else:
                    # first node conflict
                    if fabric[r][c] != "X":
                        # remove previous conflict
                        if fabric[r][c] in ids:
                            ids.remove(fabric[r][c])

                        fabric[r][c] = "X"
                        conflicts += 1

                    if claim["id"] in ids:
                            ids.remove(claim["id"])


    print conflicts
    print ids

f = open("./03_no_matter_how_you_slice_it/20/input.txt", "r")
input = f.readlines()
f.close()

execute(input)
