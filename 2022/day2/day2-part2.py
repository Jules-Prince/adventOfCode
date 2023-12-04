
gameFile = open("game.txt", "r")

gameLines = gameFile.readlines()


totalPoint = 0
for gameLine in gameLines :
    
    plays = gameLine.split()
    elfMove = plays[0]
    elfAdvise = plays[1]
    
    
    
    totalPoint+=point

print("Total points : ", totalPoint)