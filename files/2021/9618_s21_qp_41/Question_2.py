

def linearSearch(to_search):
    for x in range(len(arrayData)):
        if arrayData[x] == to_search: return True
    return False

def bubbleSort():
    temp = 0
    for x in range(0, len(arrayData)):
        for y in range(0, len(arrayData)-1-x):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
    
# main

global arrayData
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

integer_val = int(input("Enter an integer: "))
response = linearSearch(integer_val)
if response:
    print("[FOUND] Value was found in array")
else:
    print("[NOT_FOUND] Value does not exist in the array")

bubbleSort()
