import os

sum = 0
with open(os.getcwd() + "\\2015\\day2\\input\\wrap.txt") as file :
    line = file.readlines()

    for box in line :
        x, y, z = list(map(int, box.split("x")))
        
        square = (2 * x * y)  + (2 * y * z) + (2 * x * z)
        square += min(x * y, y * z, x * z)
        
        sum += square

print(sum)