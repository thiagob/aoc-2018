import re

def execute(input):
    
    for line in input.split('\n'):
        patterns = []

        for i in range(0, len(line)):
            p = list(line)
            p[i] = '.'
            patterns.append("".join(p))

        pattern = "|".join(patterns)

        results = re.findall(pattern, input)
        if len(results) == 2:
            print results

            a = list(results[0])
            b = list(results[1])

            for i in range(0, len(a)):
                if a[i] != b[i]:
                    del a[i]
                    del b[i]
                                
                    print "".join(a)
                    print "".join(b)
                    return True



f = open("./02_inventory_management_system/20/input.txt", "r")
input = f.read()
f.close()

execute(input)
