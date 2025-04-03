def Initialise():
    global NumberItems

    qty = int(input("Enter the quantity of numbers to input (1-20): "))
    while qty < 1 or qty > 20:
        print("Quantity must be from 1-20 only!")
        qty = int(input("Enter the quantity of numbers to input (1-20): "))

    for _ in range(qty):
        data = int(input("Enter integer to input: "))
        DataStored.append(data)
        NumberItems += 1


def BubbleSort():
    for x in range(NumberItems):
        swap = False
        for y in range(NumberItems-1-x):
            if DataStored[y] > DataStored[y+1]:
                swap = True
                DataStored[y], DataStored[y+1] = DataStored[y+1], DataStored[y]
        if not swap:
            break


def BinarySearch(DataToFind):
    low, top = 0, NumberItems
    while low <= top:
        mid = (low + top) // 2
        if DataStored[mid] == DataToFind:
            return mid
        if DataToFind > DataStored[mid]:
            low = mid + 1
        else:
            top = mid - 1
    return -1

# main

DataStored = [] # INTEGER
NumberItems = 0


Initialise()
print(DataStored)

BubbleSort()
print(DataStored)

to_search = int(input("Enter an integer value to search for: "))
response = BinarySearch(to_search)
print(response)
