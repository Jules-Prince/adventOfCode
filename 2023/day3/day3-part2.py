class Number:
    def __init__(self, value, xStart, xEnd, y):
        self.value = value
        self.xStart = xStart
        self.xEnd = xEnd
        self.y = y

    def __str__(self):
        return f"Number(value={self.value}, xStart={self.xStart}, xEnd={self.xEnd}, y={self.y})"


class Symbol:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y

    def __str__(self):
        return f"Symbol(symbol={self.symbol}, x={self.x}, y={self.y})"


numbers = []
symbols = []

with open('input/engineSchematics.txt', 'r') as file:
    for y, line in enumerate(file):
        xStart = None
        value = ''
        for x, char in enumerate(line.strip()):
            if char.isdigit():
                if xStart is None:
                    xStart = x
                value += char
            elif value:
                numbers.append(Number(int(value), xStart, x - 1, y))
                xStart = None
                value = ''

            if char == '*' and not char.isdigit():
                symbols.append(Symbol(char, x, y))
        if value:
            numbers.append(Number(int(value), xStart, x, y))


def get_symbol_nearby(x, y):
    for symbol in symbols:
        if abs(symbol.x - x) <= 1 and abs(symbol.y - y) <= 1:
            return symbol
    return None


numbers_connected_to_symbols = []
for symbol in symbols:
    adjacent_numbers = [number for number in numbers if
                        get_symbol_nearby(number.xStart, number.y) == symbol or get_symbol_nearby(number.xEnd,
                                                                                                  number.y) == symbol]
    if len(adjacent_numbers) == 2:
        numbers_connected_to_symbols.append(adjacent_numbers)

total = 0
for number_pair in numbers_connected_to_symbols:
    for i, number in enumerate(number_pair):
        currentRatio = number_pair[0].value * number_pair[1].value
    total += currentRatio

print(total)
