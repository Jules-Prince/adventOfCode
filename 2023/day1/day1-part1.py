import re

calibrationFile = open('calibrationInput.txt', 'r')
 
calibartionsLines = calibrationFile.readlines()
 
sumOfCalibrations = 0

for calibrationLine in calibartionsLines:
    for char is 
    calibration = re.sub("[^0-9]", "", calibrationLine)

    calibration = int(calibration[0]+calibration[-1])
    
    sumOfCalibrations += calibration

print("The amount of calibration is : ", sumOfCalibrations)