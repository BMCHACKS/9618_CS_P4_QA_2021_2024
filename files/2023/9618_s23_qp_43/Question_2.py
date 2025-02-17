
class Vehicle:
    def __init__(self, ID, MaxSpeed, InceraseAmount):
        self.__ID = ID # DECLARE PRIVATE ID : STRING
        self.__MaxSpeed = MaxSpeed # DECLARE PRIVATE  MaxSpeed : INTEGER
        self.__CurrentSpeed = 0 # DECLARE PRIVATE CurrentSpeed : INTEGER
        self.__IncreaseAmount = InceraseAmount # DECLARE PRIVATE IncreaseAmount : INTEGER
        self.__HorizontalPosition = 0 # DECLARE PRIVATE HorizontalPosition : INTEGER
    
    def GetCurrentSpeed(self): return self.__CurrentSpeed
    def GetIncreaseAmount(self): return self.__IncreaseAmount
    def GetHorizontalPosition(self): return self.__HorizontalPosition
    def GetMaxSpeed(self): return self.__MaxSpeed

    def SetCurrentSpeed(self, v): self.__CurrentSpeed = v
    def SetHorizontalPosition(self, v): self.__HorizontalPosition = v

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed: self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed


class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, InceraseAmount, VerticalChange, MaximumHeight):
        super().__init__(ID, MaxSpeed, InceraseAmount)
        self.__VerticalPosition = 0 # DECLARE PRIVATE VerticalPosition : INTEGER
        self.__VerticalChange = VerticalChange # DECLARE PRIVATE VerticalChange : INTEGER
        self.__MaxHeight = MaximumHeight # DECLARE PRIVATE MaxHeight : INTEGER


    def GetVerticalPosition(self): return self.__VerticalPosition

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight: self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()


def OutputInfo(the_object, object_type):
    main_msg = f"The Horizontal Position is: {the_object.GetHorizontalPosition()}. The Speed is: {the_object.GetCurrentSpeed()}. "
    if object_type == "Helicopter":
        print(main_msg + f"The Vertical Position is: {the_object.GetVerticalPosition()}")
    else:
        print(main_msg)
    

# main



car = Vehicle("Tiger", 100, 20)
helicopter = Helicopter("Lion", 350, 40, 3, 100)

car.IncreaseSpeed()
car.IncreaseSpeed()

OutputInfo(car, "Vehicle")

helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
OutputInfo(helicopter, "Helicopter")

