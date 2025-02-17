

def ReadFile():
    try:
        file = open("IntegerData.txt", "r")
        for x in range(100): DataArray[x] = int(file.readline().rstrip())
        
    except IOError:
        print("[ERROR] File Not Found")


def FindValues():
    to_search = int(input("Enter an integer to search for: "))
    counter = 0
    for integer in DataArray: 
        if to_search == integer: counter += 1
    return counter


def BubbleSort():
    for x in range(len(DataArray)):
        swap = False
        for y in range(len(DataArray)-1-x):
            if DataArray[y] > DataArray[y+1]: 
                DataArray[y], DataArray[y+1] = DataArray[y+1], DataArray[y]
                swap = True
        if not swap: break


# main

DataArray = [0 for _ in range(100)]

ReadFile()
response = FindValues() 
print(f"The number to search appeared this many times: {response}")

BubbleSort()
for integer in DataArray: print(integer)
