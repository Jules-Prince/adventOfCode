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

            if char != '.' and not char.isdigit():
                symbols.append(Symbol(char, x, y))
        if value:
            numbers.append(Number(int(value), xStart, x, y))


def has_symbol_nearby(x, y):
    for symbol in symbols:
        if abs(symbol.x - x) <= 1 and abs(symbol.y - y) <= 1:
            return True
    return False


sum_numbers_without_symbols = 0
for number in numbers:
    if has_symbol_nearby(number.xStart, number.y) or has_symbol_nearby(number.xEnd, number.y):
        sum_numbers_without_symbols += number.value

print(sum_numbers_without_symbols)
