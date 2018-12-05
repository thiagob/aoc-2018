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
                    "minutes_slepping": 0,
                    "records": [0 for x in range(60)]
                }

        if line.endswith('falls asleep'):
            guards[guard]["splet_at"] = minutes

        if line.endswith('wakes up'):
            guards[guard]["minutes_slepping"] += minutes - \
                guards[guard]["splet_at"]

            for i in range(guards[guard]["splet_at"], minutes):
                guards[guard]["records"][i] += 1

            guards[guard]["splet_at"] = 0

    # find worst guard
    max = 0
    worst_guard = 0
    for g in guards:
        if guards[g]["minutes_slepping"] > max:
            worst_guard = g

    max = 0
    worst_minute = 0
    for m in range(0,60):
        if guards[worst_guard]["records"][m] > max:
            max = guards[worst_guard]["records"][m]
            worst_minute = m


    print int(worst_guard) * worst_minute


f = open("./04_repose_record/10/input.txt", "r")
data = f.readlines()
data.sort()
f.close()

execute(data)
