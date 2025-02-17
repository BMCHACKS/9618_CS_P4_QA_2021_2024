def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
        IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray):
    for i in range(len(IntegerArray)):
        key, j = IntegerArray[i], i-1
        while j >= 0 and key < IntegerArray[j]:
            IntegerArray[j+1] = IntegerArray[j]
            j -= 1
        IntegerArray[j+1] = key
    return IntegerArray


def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    else:
        mid = (First + Last) // 2
        if IntegerArray[mid] == ToFind:
            return mid
        else:
            if ToFind > IntegerArray[mid]: 
                return BinarySearch(IntegerArray, mid + 1, Last, ToFind)
            if ToFind < IntegerArray[mid]: 
                return BinarySearch(IntegerArray, First, mid - 1, ToFind)


# main
NumberArray = [100, 85, 644, 22, 15, 8, 1]

NumberArray = RecursiveInsertion(NumberArray, len(NumberArray))
print("Recursive")
print(NumberArray)

NumberArray = [100, 85, 644, 22, 15, 8, 1]

NumberArray = IterativeInsertion(NumberArray)
print("iterative")
print(NumberArray)


pos = BinarySearch(NumberArray, 0, len(NumberArray)-1, 644)
if pos == -1:
    print("Not Found")
else:
    print(f"Index: {pos}")
    