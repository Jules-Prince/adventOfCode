
sum = 0

with open('/Users/julesprince/Library/Mobile Documents/com~apple~CloudDocs/Devs/adventOfCode/2023/day9/input/values.txt', 'r') as file:
    lines = file.readlines()
    
    for line in lines :
        allValues = []
        values = line.split()
        values = [eval(i) for i in values]
        allValues.append(values)
        nextValues = []
        a = 0;
        while len(nextValues) == 0 or not all(nextValue == 0 for nextValue in nextValues) :
            nextValues = []
            currentValues = allValues[a]
            for i, value in enumerate(currentValues) :
                if not (i+1>=len(currentValues))  :
                    diff = currentValues[i+1] - value
                    nextValues.append(diff)
            allValues.append(nextValues)
            a+=1
        
        allValues.pop()
        computeValue = 0
        for listValues in reversed(allValues):
            computeValue = listValues[-1] + computeValue
            print("for list :", listValues, " compute value : ", computeValue)
    
        sum+=computeValue
print("result : ", sum)