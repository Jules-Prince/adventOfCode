
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
    for line in file:
        if line.startswith("Time:"):
            timeMerged = "".join(line.split()[1:])
        elif line.startswith("Distance:"):
            distanceMerged = "".join(line.split()[1:])
    
    timePossible = computeTimeForRecord(int(timeMerged), int(distanceMerged))
    print(len(timePossible))