DataArray = [0 for _ in range(100)]

def ReadFile():
    try:
        file = open("IntegerData.txt", 'r')
        for x in range(100):
            DataArray[x] = int(file.readline().rstrip())
        file.close()
    except IOError:
        print("File does not exist!")

def FindValues():
    value = input("Enter a number (1-100): ")
    # EXAMINERS ANSWER WILL EITEHER BE Try statement or simple if statement
    while not value.isnumeric() or int(float(value)) > 100 and int(float(value) < 1):
        print("VALUE MUST BE A WHOLE NUMBER")
        value = input("Enter a number (1-100): ")
    value = int(value)
    count = 0
    for x in DataArray:
        if x == value: count += 1
    return count

def BubbleSort():
    for x in range(len(DataArray)):
        for y in range(len(DataArray)-x-1):
            swap = False
            if DataArray[y] > DataArray[y+1]: swap, DataArray[y], DataArray[y+1] = True, DataArray[y+1], DataArray[y]
        if not swap: break
    


ReadFile()
print(f"The number was repeated this many times: {FindValues()} ")

BubbleSort()
print(DataArray)
