import os

def testPair(string) :
    for i in range(len(string)-1) :
        if string.count(string[i:i+2]) > 1 :
            return True
    return False

def testOverlap(string) :
    for i in range(len(string)-2) :
        if string[i] == string[i+2] :
            return True
    return False

def testRepeat(string) :
    for i in range(len(string)-2) :
        if string[i] == string[i+2] :
            return True
    return False

sumString = 0
with open(os.getcwd() + "\\2015\\day5\\input\\letters.txt") as file :
    strings = file.readlines()
    for string in strings :
        if testPair(string) and testOverlap(string) and testRepeat(string):
            sumString += 1
print(sumString)