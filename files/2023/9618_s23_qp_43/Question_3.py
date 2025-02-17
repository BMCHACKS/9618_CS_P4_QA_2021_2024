

def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer -= 1
        return ReturnData

def ReadData():
    try:
        file = open("AnimalData.txt", 'r')
        for animal in file:
            response = PushAnimal(animal.rstrip())
            if response == False:
                print("[ERROR] Animal stack is full")            
    except IOError:
        print("[ERROR] File Not Found")
    
    try:
        file2 = open("ColourData.txt", 'r')
        for colour in file2: 
            response = PushColour(colour.rstrip())
            if response == False:
                print("[ERROR] Colour stack is full")
    except IOError:
        print("[ERROR] File Not Found")


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer-1]
        ColourTopPointer -= 1
        return ReturnData


def OutputItem():
    animal = PopAnimal()
    colour = PopColour()
    if colour != "" and animal != "":
        print(f"{colour} {animal}")
    
    if colour == "":
        response = PushAnimal(animal)
        print("No colour")
    
    if animal == "":
        response = PushColour(colour)
        print("No animal")


# main

Animal = ["" for _ in range(20)]
Colour = ["" for _ in range(10)]
AnimalTopPointer = 0
ColourTopPointer = 0

ReadData()
for _ in range(4): OutputItem()

