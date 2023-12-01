file = open("calories.txt", "r")
lines = file.readlines()

currentElf = 1
maxElf = 1
maxCalories = 0
currentCalories = 0
for line in lines:
    if line == "\n":
        currentElf += 1
        if currentCalories > maxCalories:
            maxCalories = currentCalories
            maxElf = currentElf
        currentCalories = 0
        continue
    
    currentCalories += int(line)

print("Elf " , str(maxElf), " has eaten the most calories: ", str(maxCalories))