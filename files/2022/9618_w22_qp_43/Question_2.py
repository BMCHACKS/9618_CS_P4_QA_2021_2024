
class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number # DECLARE PRIVATE Number : INTEGER
        self.__Colour = Colour # DECLARE PRIVATE Colour : STRING
    
    def GetNumber(self): return self.__Number
    def GetColour(self): return self.__Colour

class Hand:
    def __init__(self, card1, card2, card3, card4, card5):
        self.__Cards = [card1, card2, card3, card4, card5] # DECLARE PRIVATE Cards : ARRAY[0:4] OF Card
        self.__FirstCard = 0 # DECLARE PRIVATE FirstCard : INTEGER
        self.__NumberCards = 5 # DECLARE PRIVATE NumberCards : INTEGER
    
    def GetCard(self, v): return self.__Cards[v]


def CalculateValue(players_hand):
    score = 0
    for x in range(5):
        colour = players_hand.GetCard(x).GetColour()
        num = players_hand.GetCard(x).GetNumber()
        match colour:
            case 'red' : score += 5
            case 'blue' : score += 10
            case 'yellow' : score += 15
        score += num
    return score

# main

red_card_1 = Card(1, 'red')
red_card_2 = Card(2, 'red')
red_card_3 = Card(3, 'red')
red_card_4 = Card(4, 'red')
red_card_5 = Card(5, 'red')


blue_card_1 = Card(1, 'blue')
blue_card_2 = Card(2, 'blue')
blue_card_3 = Card(3, 'blue')
blue_card_4 = Card(4, 'blue')
blue_card_5 = Card(5, 'blue')


yellow_card_1 = Card(1, 'yellow')
yellow_card_2 = Card(2, 'yellow')
yellow_card_3 = Card(3, 'yellow')
yellow_card_4 = Card(4, 'yellow')
yellow_card_5 = Card(5, 'yellow')


player_1 = Hand(red_card_1, red_card_2, red_card_3, red_card_4, yellow_card_1)
player_2 = Hand(yellow_card_2, yellow_card_3, yellow_card_4, yellow_card_5, blue_card_1)


score_1 = CalculateValue(player_1)
score_2 = CalculateValue(player_2)

if score_1 > score_2: 
    print(f"Player 1 won with the score of: {score_1}")
elif score_1 < score_2:
    print(f"Player 2 won with the score of: {score_2}")
else:
    print(f"Both players have equal points! It's a DRAW")
