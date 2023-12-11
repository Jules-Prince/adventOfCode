import re

inputList = open("input/map.txt").read().splitlines()
nodeList = {}
direction = list(inputList[0])
curr = "AAA"
steps = 0

for i in inputList[2:]:
    a = re.split(r"[\W]+", i)
    nodeList[a[0]] = (a[1], a[2])

while (True):
    for u in direction:
        steps += 1
        nodeTuple = nodeList.get(curr)
        if u == "L":
            curr = nodeTuple[0]
        else:
            curr = nodeTuple[1]

        if curr == "ZZZ":
            break
    
    else:
        continue
    break

print(steps)
