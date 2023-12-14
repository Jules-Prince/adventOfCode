import os

with open(os.getcwd() + "\\2015\\day1\\input\\elevation.txt") as file :
    floor = 0
    line = file.readlines()

    for elevator in line :
        for i, char in enumerate(elevator) :
            if floor == -1 :
                print(i)
                break
            if char == "(" :
                floor += 1
            elif char == ")" :
                floor -= 1
            
            
