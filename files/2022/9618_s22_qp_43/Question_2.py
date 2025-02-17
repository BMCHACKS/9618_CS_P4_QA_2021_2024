
class Balloon:
    def __init__(self, defence_item, colour):
        self.__Health = 100 # DECLARE PRIVATE Health : INTEGER
        self.__Colour = colour # DECLARE PRIVATE Colour : STRING
        self.__DefenceItem = defence_item # DECLARE PRIVATE DefenceItem : STRING
    
    def ChangeHealth(self, v): self.__Health += v
    def GetDefenseItem(self): return self.__DefenceItem
    def CheckHealth(self): return self.__Health <= 0

def Defend(balloonobj):
    strength = int(input("Enter opponent's strength: "))
    balloonobj.ChangeHealth(-strength)
    defence_item = balloonobj.GetDefenseItem()
    print(defence_item)
    health_check = balloonobj.CheckHealth()
    if health_check:
        print("[YOU LOSE] Balloon has no health remaining!")
    else:
        print("[SURVIVED] Balloon still has health left")
    return balloonobj


# main

item = input("Enter your defence item: ")
colour = input("Enter your colour: ")

Balloon1 = Balloon(item, colour)

Defend(Balloon1)
