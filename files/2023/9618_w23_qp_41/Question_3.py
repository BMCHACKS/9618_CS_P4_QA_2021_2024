class Character:
    def __init__(self, n, x, y):
        self.__Name = n
        self.__XPositon = x
        self.__YPositon = y
    def GetXPosition(self): return self.__XPositon      
    def GetYPosition(self): return self.__YPositon        
    def SetXPosition(self, v): self.__XPositon = 10000 if v + self.__XPositon > 10000 else 0 if v + self.__XPositon < 0 else v + self.__XPositon   
    def SetYPosition(self, v): self.__YPositon = 10000 if v + self.__YPositon > 10000 else 0 if v + self.__YPositon < 0 else v + self.__YPositon        
    def Move(self, v):
        match v:
            case 'up' : self.SetYPosition(10)
            case 'down' : self.SetYPosition(-10)
            case 'left' : self.SetXPosition(-10)
            case 'right' : self.SetXPosition(10)

class BikeCharacter(Character):
    def __init__(self, n, x, y):
        super().__init__(n, x, y)
    
    def Move(self, v):
        match v:
            case 'up' : super().SetYPosition(20)
            case 'down' : super().SetYPosition(-20)
            case 'left' : super().SetXPosition(-20)
            case 'right' : super().SetXPosition(20)
        

Jack = Character("Jack", 50, 50)
Karla = BikeCharacter("Karla", 100, 50)

Char = input("Which character do you want to move (Jack or Karla): ")

while Char != "Jack" and Char != "Karla":
    print("WRONG CHOICE!!!")
    Char = input("Which character do you want to move (Jack or Karla): ")

direction = input("Enter diraction to move (up, down, left, right): ")

while direction not in ['up', 'down', 'left', 'right']:
    print("WRONG DIRECTION!")
    direction = input("Enter diraction to move (up, down, left, right): ")


if Char == 'Jack':
    Jack.Move(direction)
    print(f"Jack's new postion is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
else:
    Karla.Move(direction)
    print(f"Karla's new postion is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")


