import os

nbHouses = 1
with open(os.getcwd() + "\\2015\\day3\\input\\house.txt") as file :
    line = file.readline()
    
    x, y = 0, 0
    housesVisited = []
    housesVisited.append((x, y))
    for char in line :
        match char :
            case "^" :
                y+=1
            case "v" :
                y-=1
            case "<" :
                x-=1
            case ">" :
                x+=1
        if (x, y) not in housesVisited :
            housesVisited.append((x, y))
            nbHouses+=1
print(nbHouses)