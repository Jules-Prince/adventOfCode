import os

sumFuel = 0
with open(os.path.dirname(__file__) + '/input/mass.txt', 'r') as file :
    mass = file.readlines()
    
    
    for m in mass:
        currentFuel = int(m) // 3 - 2
        while not currentFuel < 0 :
            sumFuel += currentFuel
            currentFuel = int(currentFuel) // 3 - 2

print(sumFuel)