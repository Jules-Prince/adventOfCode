import os
sum=0
with (open(os.path.dirname(__file__) + '/input/instruction.txt', 'r')) as file:
    lines = file.readlines()
    lightGrid = [[0 for x in range(1000)] for y in range(1000)]
    for line in lines:
        
        if "turn on" in line :
            line = line.replace("turn on ", "")
            line = line.replace("through ", "")
            
            start = tuple(map(int, line.split(" ")[0].split(",")))
            end = tuple(map(int, line.split(" ")[1].split(",")))
            
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    lightGrid[x][y] += 1 
        elif "turn off" in line :
            line = line.replace("turn off ", "")
            line = line.replace("through ", "")
            start = tuple(map(int, line.split(" ")[0].split(",")))
            end = tuple(map(int, line.split(" ")[1].split(",")))
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    lightGrid[x][y] -= 1 if lightGrid[x][y] > 0 else 0
        elif "toggle" in line : 
            line = line.replace("toggle ", "")
            line = line.replace("through ", "")
            start = tuple(map(int, line.split(" ")[0].split(",")))
            end = tuple(map(int, line.split(" ")[1].split(",")))
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    lightGrid[x][y] += 2

for sublist in lightGrid:
    for element in sublist:
            sum += element
print(sum)