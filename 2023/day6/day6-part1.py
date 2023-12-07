
races = {}

def computeTimeForRecord(raceTime, recordDistance):
    timePossible = [];
    for time in range(raceTime) :
        speed = time
        distance = speed * (raceTime - time)

        if distance > recordDistance :
            timePossible.append(time)
    return timePossible

with open('input/races.txt', 'r') as file:
    lines = file.readlines()
    time_values = lines[0].split()[1:]  
    distance_values = lines[1].split()[1:]  
    
    for time, distance in zip(time_values, distance_values):
        races[int(time)] = int(distance)
    
    numbersOfTimeToWin = [];
    for raceKey, raceValue in races.items():
        timePossible = computeTimeForRecord(raceKey, raceValue)
        numbersOfTimeToWin.append(len(timePossible))
    
    prod = 1
    for i in numbersOfTimeToWin:
        prod = prod*i
    print(prod)