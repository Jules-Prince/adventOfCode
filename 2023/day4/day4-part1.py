total = 0
copies = []
with open('input/test.txt', 'r') as file:
    for i, card in enumerate(file):
        cardNumber, cardNumbers = card.split(':')

        cardNumber = int(cardNumber.replace('Card ', ''))
        # Split the card numbers at the pipe symbol
        winingNumbers, gameNumbers = cardNumbers.split('|')

        # Convert the numbers before the pipe symbol to a list of integers
        winingNumbers = list(map(int, winingNumbers.split()))
        gameNumbers = list(map(int, gameNumbers.split()))

        currentPoints = 1
        currentWeight = 1
        for gameNumber in gameNumbers :
            if gameNumber in winingNumbers :
                if currentWeight > 1 :
                    currentPoints *= 2

                currentWeight+=1
        if currentWeight!=1 :
            total+=currentPoints
print(total)