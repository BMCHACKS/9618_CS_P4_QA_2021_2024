class Vehicle:
    # self.__ID : STRING
    # self.__CurrentSpeed : INTEGER
    # self.__MaxSpeed : INTEGER
    # self.__IncreaseAmount : INTEGER
    # self.__HorizontalPosition : INTEGER
    def __init__(self, ID, MaxSpeed, IncereaseAmount):
        self.__ID = ID
        self.__CurrentSpeed = 0
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncereaseAmount
        self.__HorizontalPosition = 0
    def GetCurrentSpeed(self): return self.__CurrentSpeed
    def GetIncreaseAmount(self): return self.__IncreaseAmount
    def GetHorizontalPosition(self): return self.__HorizontalPosition
    def GetMaxSpeed(self): return self.__MaxSpeed

    def SetCurrentSpeed(self, v): self.__CurrentSpeed = v
    def SetHorizontalPosition(self, v): self.__HorizontalPosition = v

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount if self.__CurrentSpeed + self.__IncreaseAmount <= self.__MaxSpeed else self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncereaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncereaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange if self.__VerticalPosition + self.__VerticalChange <= self.__MaxHeight else self.__MaxHeight
        super().IncreaseSpeed()
    def GetVerticalPosition(self): return self.__VerticalPosition

def OutputInfo(classobj, classofobj):
    print(f"The Horizontal Position is: {classobj.GetHorizontalPosition()}")
    if classofobj == 'Helicopter': print(f"The Vertical Position is: {classobj.GetVerticalPosition()}")
    print(f"The Speed is: {classobj.GetCurrentSpeed()}")



Car = Vehicle('Tiger', 100, 20)
Heli = Helicopter('Lion', 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
OutputInfo(Car, 'Vechicle')
Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
OutputInfo(Heli, 'Helicopter')

