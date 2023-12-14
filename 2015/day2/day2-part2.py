import os

sum = 0
with open(os.getcwd() + "\\2015\\day2\\input\\wrap.txt") as file :
    line = file.readlines()

    for box in line :
        x, y, z = list(map(int, box.split("x")))
        
        ribbon = 2 * (x + y + z - max(x, y, z)) + x * y * z

        sum += ribbon

print(sum)