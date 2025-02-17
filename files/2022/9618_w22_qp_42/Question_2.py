
class Character:
    def __init__(self, Name, XCoordinate, YCoordiante):
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordinate = YCoordiante

    def GetName(self): return self.__Name
    def GetX(self): return self.__XCoordinate
    def GetY(self): return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange
    
# main

Character_Array =  []

try:
    file = open('Characters.txt', 'r')
    for line in file:
        name = line.rstrip()
        x_cord = int(file.readline().rstrip())
        y_cord = int(file.readline().rstrip())
        Character_Array.append(Character(name, x_cord, y_cord))
except IOError:
    print("[ERROR] File Not Found")


valid_character = False
while not valid_character:
    name = input("Enter Name of Character: ")
    for x in range(len(Character_Array)):
        if Character_Array[x].GetName().lower() == name.lower(): 
            index = x
            valid_character = True
    if not valid_character: print("[ERROR] That character name does not exist!")
    

valid_move = False
while not valid_move:
    move = input("Enter move [W, A, S, D]: ")
    if move in ['W', 'A', 'S', 'D']: 
        valid_move = True
    else:
        print("[ERROR] Not a valid move!")

match move:
    case 'A' : Character_Array[x].ChangePosition(-1, 0)
    case 'W' : Character_Array[x].ChangePosition(0, 1)
    case 'S' : Character_Array[x].ChangePosition(0, -1)
    case 'D' : Character_Array[x].ChangePosition(1, 0)

char_name =  Character_Array[x].GetName()
x_pos = Character_Array[x].GetX()
y_pos = Character_Array[x].GetY()

print(f"{char_name} has changed coordinates to X = {x_pos} and Y = {y_pos}")

