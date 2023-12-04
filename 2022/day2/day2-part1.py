
gameFile = open("game.txt", "r")

gameLines = gameFile.readlines()

moves = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
totalPoint = 0
for gameLine in gameLines :
    
    plays = gameLine.split()
    elfMove = plays[0]
    myMove = plays[1]
    
    point = moves[myMove]
    
    #WIN
    points = {
        ("X", "C"): 6,
        ("Y", "A"): 6,
        ("Z", "B"): 6,
        ("X", "A"): 3,
        ("Y", "B"): 3,
        ("Z", "C"): 3,
    }
    
    point += points.get((myMove, elfMove), 0)
    
    totalPoint+=point

print("Total points : ", totalPoint)