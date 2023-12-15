import os

allHash = 0
with open(os.path.dirname(__file__) + '/input/hash.txt', 'r') as file :
    lines = file.readline()
    strings = lines.split(",")

    for string in strings :
        hash = 0
        for char in string :
            hash += ord(char)
            hash *= 17
            hash %= 256
        allHash+=hash

print(allHash)