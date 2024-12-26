DataArray = []

try:
    with open("Data.txt") as file:
        for data in file:
            DataArray.append(int(data.rstrip()))
except IOError:
    print("File does not exist!")


def PrintArray(intArray):
    for val in intArray: print(val, end=' ')
    print()


def LinearSearch(intArray, to_search):
    counter = 0
    for val in intArray: 
        if val == to_search: counter += 1
    return counter


# main
PrintArray(DataArray)

to_search = int(input("Enter a value (0-100) inclusive: "))
while to_search > 100 or to_search < 0:
    print("Value Should be in range!")
    to_search = int(input("Enter a value (0-100) inclusive: "))
    
print(f"The number {to_search} was found {LinearSearch(DataArray, to_search)} times.")


