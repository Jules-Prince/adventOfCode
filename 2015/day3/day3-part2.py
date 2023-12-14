import os

nbHouses = 1
with open(os.getcwd() + "\\2015\\day3\\input\\house.txt") as file :
    line = file.readline()
    
    housesVisited = set()
xSanta, ySanta = 0, 0
xRobotSanta, yRobotSanta = 0, 0
housesVisited.add((0, 0))
for i in range(0, len(line), 2):
    if i + 1 >= len(line):
        break
    
    # Update Santa's position
    xSanta += {"^": 0, "v": 0, "<": -1, ">": 1}[line[i]]
    ySanta += {"^": 1, "v": -1, "<": 0, ">": 0}[line[i]]
    
    if (xSanta, ySanta) not in housesVisited:
        housesVisited.add((xSanta, ySanta))
    
    # Update Robot Santa's position
    xRobotSanta += {"^": 0, "v": 0, "<": -1, ">": 1}[line[i + 1]]
    yRobotSanta += {"^": 1, "v": -1, "<": 0, ">": 0}[line[i + 1]]
    
    if (xRobotSanta, yRobotSanta) not in housesVisited:
        housesVisited.add((xRobotSanta, yRobotSanta))
nbHouses = len(housesVisited)
print(nbHouses)