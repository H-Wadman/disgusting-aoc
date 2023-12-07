

TEST_INPUT = 8
REAL_INPUT = 10

file = open("input.txt", "r")
lines = file.readlines()

data = [x[REAL_INPUT:].strip() for x in lines]

CARD_WIN = 0
CARD_GOT = 1

data = [card.split('|') for card in data]
data = [[a.split(), b.split()] for [a, b] in data]

def calculate_points(card_num):
    card = data[card_num]
    winning, obtained = card
    match = 0
    for num in obtained:
        if num in winning:
             match += 1
    
    return match

backtrack = []

res = 0

res += len(data)

for i, card in enumerate(data):
    match = calculate_points(i)
    if match != 0:
        res += match
        backtrack.append((i, match))


while bool(backtrack):
    n, match = backtrack.pop()

    for i in range(n + 1, n + match + 1):
        score = calculate_points(i)
        if score != 0:
            res += score
            backtrack.append((i, score))


print(res)