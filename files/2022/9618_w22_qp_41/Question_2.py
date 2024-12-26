class Card:
    #self.__Number : INTEGER
    #self.__Colour : STRING
    def __init__(self, n, c):
        self.__Number = n
        self.__Colour = c
    def GetNumber(self): return self.__Number
    def GetColour(self): return self.__Colour

class Hand:
    #self.__Cards : ARRAY[0:9] OF Card
    #self.__FirstCard : INTEGER
    #self.__NumCards : INTEGER
    def __init__(self, c1, c2, c3, c4, c5):
        self.__Cards = [c1, c2, c3, c4, c5]
        self.__FirstCard = 0
        self.__NumCards = 5
    def GetCard(self, pos): return self.__Cards[pos]

def CalculateValue(PlayerHand):
    Total_Score = 0
    players_cc = [[PlayerHand.GetCard(x).GetNumber(), PlayerHand.GetCard(x).GetColour()] for x in range(5)]
    for card in players_cc:
        if card[1] == 'red': Total_Score += 5
        if card[1] == 'blue': Total_Score += 10
        if card[1] == 'yellow': Total_Score += 15
        Total_Score += card[0]
    return Total_Score

# main 
c1 = Card(1, "red")
c2 = Card(2, "red")
c3 = Card(3, "red")
c4 = Card(4, "red")
c5 = Card(5, "red")

c6 = Card(1, "blue")
c7 = Card(2, "blue")
c8 = Card(3, "blue")
c9 = Card(4, "blue")
c10 = Card(5,"blue")

c11 = Card(1, "yellow")
c12 = Card(2, "yellow")
c13 = Card(3, "yellow")
c14 = Card(4, "yellow")
c15 = Card(5, "yellow")


player_1 = Hand(c1, c2, c3, c4, c11)
player_2 = Hand(c12, c13, c14, c15, c6)

p1v = CalculateValue(player_1)
p2v = CalculateValue(player_2)
print(f"Player 1 won with {p1v} points" if p1v > p2v else f"Player 2 won with {p2v} points" if p2v > p1v else f"It was a draw")

