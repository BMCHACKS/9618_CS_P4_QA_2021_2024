class Balloon:
    def __init__(self, defence_item, colour):
        self.__Health = 100
        self.__Colour = colour
        self.__DefenceItem = defence_item
    def GetDefenceItem(self): return self.__DefenceItem
    def ChangeHealth(self, v): self.__Health += v
    def CheckHealth(self): return self.__Health <= 0


def Defend(balloonobj):
    strength = int(input("Enter the strength of the opponent: "))
    balloonobj.ChangeHealth(-strength)
    print(balloonobj.GetDefenceItem())
    if balloonobj.CheckHealth():
        print("The balloon has no health :(")
    else:
        print("The balloon has health remaining!")
    return balloonobj

# main
defence_item = input('Enter a defence item: ')
Ballon_colour = input("Enter your Balloon's colour: ")
Balloon1 = Balloon(defence_item, Ballon_colour)
Balloon1 = Defend(Balloon1)
