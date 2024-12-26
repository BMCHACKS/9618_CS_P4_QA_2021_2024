arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(val: int):
    for value in arrayData: 
        if val == value: return True
    return False


val = int(input("Enter value to search: "))
print("Value found!") if linearSearch(val) else print("Value not found!")


def bubbleSort():
    for x in range(10):
        for y in range(9):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
    


