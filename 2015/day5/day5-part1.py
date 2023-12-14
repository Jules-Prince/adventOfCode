import os

def testVowels(string) :
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for vowel in vowels :
        count += string.count(vowel)
    return count >= 3

def testDoubleLetter(string) :
    for i in range(len(string)-1) :
        if string[i] == string[i+1] :
            return True
    return False

def testForbidden(string) :
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for forbid in forbidden :
        if forbid in string :
            return False
    return True

sumString = 0
with open(os.getcwd() + "\\2015\\day5\\input\\letters.txt") as file :
    strings = file.readlines()
    for string in strings :

        if testVowels(string) and testDoubleLetter(string) and testForbidden(string) :
            sumString+=1
print(sumString)