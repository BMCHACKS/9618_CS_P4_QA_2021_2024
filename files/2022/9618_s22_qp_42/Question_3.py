class Card:
    def __init__(self, num : int, col : str) -> None:
        self.__Number = num
        self.__Colour = col
    
    def GetNumber(self) -> int: return self.__Number
    def GetColour(self) -> str: return self.__Colour

CardArray = []
try:    
    file = open("CardValues.txt", 'r')
    for num in file:
        col = file.readline()
        CardArray.append(Card(num.rstrip(), col.rstrip()))
except IOError:
    print("File Error!")


Card_Picked_idx = []

def ChooseCard() -> int:
    val = int(input("Enter the card index(1-30): "))
    def check_range(val : int) -> bool:
        if val >= 1 and val <= 30: return True
        return False
    
    while val in Card_Picked_idx or not check_range(val):
        val = int(input("[ERROR] Card already picked or Card index out of range(1 - 30) | Enter new: "))

    Card_Picked_idx.append(val)
    return val

Player1 = [CardArray[ChooseCard()] for _ in range(4)]
for x in Player1: print(f"{x.GetNumber()} | {x.GetColour()}")