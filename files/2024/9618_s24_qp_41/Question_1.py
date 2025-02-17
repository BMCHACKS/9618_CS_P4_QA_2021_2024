
def Initialise():
    numbers = int(input("Enter the quantity of numbers to enter: "))
    for _ in range(numbers): 
        while True:
            n = int(input("Enter a number(1-20): "))
            if n >= 1 and n <= 20: break
            print("Number must be between 1 - 20 inclusive!")
        DataStored.append(n)

def BubbleSort():
    for x in range(len(DataStored)):
        swap = False
        for y in range(len(DataStored)-1-x):
            if DataStored[y] > DataStored[y+1]: DataStored[y], DataStored[y+1], swap = DataStored[y+1], DataStored[y], True 
        if not swap: break

def BinarySearch(DataToFind):
    low, top = 0, len(DataStored)-1
    while low <= top:
        mid = (low+top) // 2
        if DataStored[mid] == DataToFind: return mid
        low = mid+1 if DataToFind > DataStored[mid] else low
        top = mid-1 if DataToFind < DataStored[mid] else top
    return -1 


# main

global NumberItems
DataStored = []
NumberItems = 0

Initialise()
print(DataStored)

BubbleSort()
print(DataStored)

n = int(input("Enter a number to search for: "))
pos = BinarySearch(n)
print(pos)

