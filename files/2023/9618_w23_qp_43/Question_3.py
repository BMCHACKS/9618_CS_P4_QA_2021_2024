class Character:
    def __init__(self, Name, XPosition, YPosition):
        self.__Name = Name # DECLARE PRIVATE Name : STRING
        self.__XPosition = XPosition # DECLARE PRIVATE XPosition : INTEGER
        self.__YPosition = YPosition # DECLARE PRIVATE  YPosition : INTEGER
    
    def GetXPosition(self): return self.__XPosition
    def GetYPosition(self): return self.__YPosition

    def SetXPosition(self, v):
        new_pos = self.__XPosition + v
        if new_pos >= 0 and new_pos <= 10000:
            self.__XPosition = new_pos
        elif new_pos > 10000:
            self.__XPosition = 10000
        elif new_pos < 0:
            self.__XPosition = 0

    def SetYPosition(self, v):
        new_pos = self.__YPosition + v
        if new_pos >= 0 and new_pos <= 10000:
            self.__YPosition = new_pos
        elif new_pos > 10000:
            self.__YPosition = 10000
        elif new_pos < 0:
            self.__YPosition = 0

    def Move(self, movement):
        match movement:
            case 'up' : self.SetYPosition(10) 
            case 'down' : self.SetYPosition(-10)
            case 'left' : self.SetXPosition(-10)
            case 'right' : self.SetXPosition(10)
        

class BikeCharacter(Character):
    def __init__(self, Name, XPosition, YPosition):
        super().__init__(Name, XPosition, YPosition)
    
    def Move(self, movement):
         match movement:
            case 'up' : super().SetYPosition(20) 
            case 'down' : super().SetYPosition(-20)
            case 'left' : super().SetXPosition(-20)
            case 'right' : super().SetXPosition(20)
        
       
# main

Jack = Character('Jack', 50, 50)
Karla = BikeCharacter('Karla', 100, 50)


while True:
    char  = input("PICK YOUR CHARACTER [jack | karla]: ").lower()
    if char == 'jack' or char == 'karla': break
    print("[ERROR] ENTER THE NAME OF THE CHARACTER ")

while True:
    move = input("Enter where to movve [up, down, left, right]: ")
    if move in ['up', 'down', 'left', 'right']: break
    print("[ERROR] Enter a valid move [up, down, left, right]")

if char == 'jack':
    Jack.Move(move)
    print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
else:
    Karla.Move(move)
    print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")

