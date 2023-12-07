import mappings as mp
def label_to_int(label):
    try:
        return int(label)
    except:
        match label:
            case "A": return 14
            case "K": return 13
            case "Q": return 12
            case "J": return 0
            case "T": return 10

def calculate_score(hand):
    cards = {}
    for char in hand:
        if char not in cards.keys():
            cards[char] = 1
        else:
            cards[char] += 1
    
    match len(cards):
        case 1: return mp.FIVE_OAK
        case 5: return mp.HIGH_CARD
        case 2:
            if 4 in cards.values():
                return mp.FOUR_OAK
            else:
                return mp.FULL_HOUSE
        case 3:
            if 3 in cards.values():
                return mp.THREE_OAK
            else:
                return mp.TWO_PAIR
        case 4:
            return mp.ONE_PAIR

def calc_score2(hand):
    cards = {}
    for char in hand:
        if char not in cards.keys():
            cards[char] = 1
        else:
            cards[char] += 1
    
    if not "J" in cards.keys():
        return calculate_score(hand)
    else:
        match len(cards):
            case 1: return mp.FIVE_OAK
            case 2: return mp.FIVE_OAK
            case 3:
                j = cards["J"]
                for val in cards.items():
                    if val[0] == "J": continue
                    else:
                        if j + val[1] == 4: return mp.FOUR_OAK
                
                return mp.FULL_HOUSE
            case 4:
                j = cards["J"]
                for val in cards.items():
                    if val[0] == "J": continue
                    else:
                        if j + val[1] == 3: return mp.THREE_OAK
                
            case 5: return mp.ONE_PAIR
        
        

file = open("input.txt", "r")

input = file.readlines()
file.close()

input = [line.split() for line in input]
input = [(hand, int(bid)) for hand, bid in input]

input = [(hand, bid, calc_score2(hand)) for hand, bid in input]

def sorting(tup):
    hand, _, score = tup

    return (score, [label_to_int(label) for label in hand])


input.sort(key=sorting)

sum = 0
for rank, tup in enumerate(input):
    rank += 1
    sum += tup[1] * rank

print(sum)