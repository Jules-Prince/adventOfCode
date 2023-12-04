import re

calibrationFile = open('inpuit/calibrationInput.txt', 'r')
 
calibartionsLines = calibrationFile.readlines()
 
sumOfCalibrations = 0

# Strips the newline character
for calibrationLine in calibartionsLines:
    pattern = r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))'
    nums = [match.group(1) for match in re.finditer(pattern, calibrationLine)]
    
    wordNums = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    if nums[0] in wordNums:
        firstNum=wordNums[nums[0]]
    else:
        firstNum=nums[0]

    if nums[-1] in wordNums:
        lastNum=wordNums[nums[-1]]
    else:
        lastNum=nums[-1]

    calibration=int(firstNum+lastNum)
    
    sumOfCalibrations += calibration

print("The amount of calibration is : ", sumOfCalibrations)