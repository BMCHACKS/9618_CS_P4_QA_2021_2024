Animal = ["" for _ in range(20)]
Colour = ["" for _ in range(10)]
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataTopPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataTopPush
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData

def ReadData():
    try:
        with open("AnimalData.txt") as file:
            for animal in file:
                PushAnimal(animal.rstrip())
        file.close()
        with open("ColourData.txt") as file:
            for colour in file:
                PushColour(colour.rstrip())
        file.close()
    except IOError:
        print("File does not exist!")

def PushColour(DataTopPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataTopPush
        ColourTopPointer += 1
        return True

def PopColor():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData
    
def OutputItem():
    ac, a = PopColor(), PopAnimal()
    if ac == "":
        PushAnimal(a)
        print("No colour")
    elif a == "":
        PushColour(ac)
        print("No Animal")
    else:
        print(f"{ac} {a}")
        

# main
ReadData()
for _ in range(4): OutputItem()

