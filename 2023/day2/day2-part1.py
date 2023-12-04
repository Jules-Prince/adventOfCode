games = open('input/games.txt', 'r')

gamesLines = games.readlines()

total = 0

for gameLine in gamesLines :
    
    gameNumber, game_data = gameLine.split(':')

    gameNumber = int(gameNumber.replace('Game ', ''))

    
    groups = game_data.split(';')
    
    groups = [group.strip() for group in groups]
    impossible = False
    for group in groups :
        cubes = group.split(",")
        redCubes = 0
        blueCubes = 0
        greenCubes = 0
        for cube in cubes:
            number, color = cube.strip().split(' ')
            number = int(number)

            if color == 'blue':
                blueCubes += number
            elif color == 'red':
                redCubes += number
            elif color == 'green':
                greenCubes += number
        
        #print(redCubes, greenCubes, blueCubes)
        if(redCubes>12 or greenCubes>13 or blueCubes>14) :
            impossible = True
            break;
        else :
            print(gameNumber)
    if(not impossible) :
        total+=gameNumber
print(total)