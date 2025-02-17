
class Picture:
    def __init__(self, description, width, height, framecolour):
        self.__Description = description # DECLARE PRIVATE Description : STRING
        self.__Width = width # DECLARE PRIVATE Width : INTEGER
        self.__Height = height # DECLARE PRIVATE Height : INTEGER
        self.__FrameColour = framecolour # DECLARE PRIVATE FrameColour : STRING
    

    def GetDescription(self): return self.__Description
    def GetHeight(self): return self.__Height
    def GetWidth(self): return self.__Width
    def GetColour(self): return self.__FrameColour

    def SetDescription(self, v): self.__Description = v

def ReadData():
    try:
        pics = 0
        file = open('Pictures.txt', 'r')
        for line in file:
            pics += 1
            description = line.rstrip()
            width = file.readline().rstrip()
            height = file.readline().rstrip()
            colour = file.readline().rstrip()
            Pictures_Array.append(Picture(description, int(width), int(height), colour))
        return pics
    except IOError:
        print("[ERROR] File Not Found")
    

# main

Pictures_Array = []
response = ReadData()


print("-- ENTER YOUR PICTURE REQUIREMENTS --")
colour = input("Enter colour of frame: ").lower()
max_width = int(input("Enter width of picture: "))
max_height = int(input("Enter colour of picture: "))

print(f"Description | Width | Height")
for pictures in Pictures_Array:
    if pictures.GetColour() == colour and pictures.GetHeight() <= max_height and pictures.GetWidth() <= max_width:
        print(f"{pictures.GetDescription()} {pictures.GetWidth()} {pictures.GetHeight()}")
        

