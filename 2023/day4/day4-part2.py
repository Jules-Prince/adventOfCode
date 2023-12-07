def add_card_copies(card_id, number_of_copies):
    if card_id + number_of_copies > len(cards):
        return
    for i in range(1, number_of_copies + 1):
        if card_id + i < len(cards):
            cardCopies.append(cards[card_id + i])

cards = [...]  # List of cards
cardCopies = []

total = 0
with open('input/test.txt', 'r') as file:
    for i, card in enumerate(file):
        cardNumber, cardNumbers = card.split(':')

        cardNumber = int(cardNumber.replace('Card ', ''))

        # Split the card numbers at the pipe symbol
        winingNumbers, gameNumbers = cardNumbers.split('|')

        # Convert the numbers before the pipe symbol to a list of integers
        winingNumbers = list(map(int, winingNumbers.split()))
        gameNumbers = list(map(int, gameNumbers.split()))

        winingNumbers = set(winingNumbers)
        gameNumbers = set(gameNumbers)

        matches = winingNumbers.intersection(gameNumbers)

        add_card_copies(cardNumber, matches)

        total_card_instances = len(cards) + len(cardCopies)
print(total_card_instances)
