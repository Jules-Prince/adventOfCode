import os

sumFuel = 0
with open(os.path.dirname(__file__) + '/input/mass.txt', 'r') as file :
    mass = file.readlines()
    
    for m in mass:
        sumFuel += int(m) // 3 - 2
print(sumFuel)