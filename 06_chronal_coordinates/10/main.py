import re

coordinates = []

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calculate_closest(position):
    distances = []

    for coordinate in coordinates:
        distances.append(manhattan_distance(position, coordinate))

    min_dist = min(distances)
    if distances.count(min_dist) >= 2:
        return None
    else:
        return distances.index(min_dist)

def export(grid):
    file = open('./06_chronal_coordinates/10/export.txt', 'w')
    
    for c in range(0, len(grid)):
        for r in range(0, len(grid)):
            file.write(str(grid[r][c]) + '\t')
        file.write('\n')
    file.close()

def execute(data):
    grid_size = max([int(s) for s in re.findall(r'\d+', "".join(data))]) + 1
    grid = [[-1 for x in range(grid_size)] for y in range(grid_size)]

    areas = []
    infinites = {}

    for item in data:
        coordinates.append([int(s) for s in re.findall(r'\d+', item)])
        areas.append(0)

    for r in range(0, len(grid)):
        for c in range(0, len(grid)):
            closest = calculate_closest([r, c])

            if closest is not None:
                grid[r][c] = closest
                
                is_infinite = (c <= 0 or r <= 0 or c >= grid_size or r >= grid_size)
                if is_infinite:
                    infinites[closest] = True
                    areas[closest] = 0
                elif closest not in infinites:
                    areas[closest] += 1

    print max(areas)
    export(grid)

f = open("./06_chronal_coordinates/input.txt", "r")
data = f.readlines()
f.close()

execute(data)
