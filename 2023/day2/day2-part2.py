games = open('input/games.txt', 'r')

gamesLines = games.readlines()

total = 0

for gameLine in gamesLines :
    
    gameNumber, game_data = gameLine.split(':')

    gameNumber = int(gameNumber.replace('Game ', ''))

    
    groups = game_data.split(';')
    
    maxRedCube = 0
    maxGreenCube = 0
    maxBlueCube = 0
    
    groups = [group.strip() for group in groups]
    impossible = False
    for group in groups :
        cubes = group.split(",")
        for cube in cubes:
            number, color = cube.strip().split(' ')
            number = int(number)

            if color == 'blue':
                maxBlueCube = max(maxBlueCube, number)
            elif color == 'red':
                maxRedCube = max(maxRedCube, number)
            elif color == 'green':
                maxGreenCube = max(maxGreenCube, number)
        
    powers = maxGreenCube * maxBlueCube * maxRedCube
    total+=powers
print(total)