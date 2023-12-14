import hashlib
import os

with open(os.getcwd() + "\\2015\\day4\\input\\hash.txt") as file :
    line = file.readline()

    i = 0
    while True :
        i+=1
        hash = hashlib.md5(f"{line}{i}".encode()).hexdigest()
        if hash.startswith("000000") :
            break
    print(i)
