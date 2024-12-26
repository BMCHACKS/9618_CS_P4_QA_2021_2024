def Initialise():
    val = int(input("Enter the quantity of numbers: "))
    while val > 20 or val < 1:
        print("[ERROR] Value out of range!")
        val = int(input("Enter the quantity of numbers: "))
    for x in range(val): DataStored.append(int(input("Enter the number to store: ")))

def BubbleSort():
    for x in range(len(DataStored)):
        for y in range(len(DataStored)-x-1): 
            Swap = False
            if DataStored[y] > DataStored[y+1]: DataStored[y], DataStored[y+1], Swap = DataStored[y+1], DataStored[y], True  
        if not Swap: break

def Binary_Search(DataToFind):
    low, top = 0, len(DataStored)-1
    while top >= low:
        mid = (low + top) // 2
        if DataStored[mid] == DataToFind: return mid
        low, top = mid + 1 if DataStored[mid] < DataToFind else low, mid - 1 if DataStored[mid] > DataToFind else top 
    return -1

# main 
DataStored = []
NumberItems = 0
Initialise()

print("BEFORE")
for val in DataStored: print(val)
BubbleSort()
print("AFTER")
for val in DataStored: print(val)

tosearch = int(input("Enter a value to search: "))
response = Binary_Search(tosearch)
print(response)
