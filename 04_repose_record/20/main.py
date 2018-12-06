import re
from datetime import datetime


def execute(data):

    guard = 0
    guards = {}

    for l in data:
        line = l.strip()
        info = re.findall(r'\d+', line)

        date = info[1] + '-' + info[2]
        minutes = int(info[4])

        if line.endswith('begins shift'):
            guard = info[5]
            if guard not in guards:
                guards[guard] = {
                    "splet_at": 0,
                    "records": [0 for x in range(59)],
                    "total_asleep": 0,
                }

        if line.endswith('falls asleep'):
            guards[guard]["splet_at"] = minutes

        if line.endswith('wakes up'):
            slepping = minutes - guards[guard]["splet_at"]
            guards[guard]["total_asleep"] += slepping

            for x in range(guards[guard]["splet_at"], minutes):
                guards[guard]["records"][x] += 1

            guards[guard]["splet_at"] = 0


    maximum = 0
    best_guard = 0
    best_minute = 0
    for guard in guards:
        for idx, val in enumerate(guards[guard]["records"]):
            if val > maximum:
                maximum = val
                best_guard = guard
                best_minute = idx

    print int(best_guard) * best_minute


f = open("./04_repose_record/10/input.txt", "r")
data = f.readlines()
data.sort()
f.close()

execute(data)
