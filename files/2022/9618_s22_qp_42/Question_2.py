import random
ArrayData = ([[random.randint(1, 100) for _ in range(10)] for _ in range(10)])

def output_array() -> list:
    for data in ArrayData: print(data)

output_array()

ArrayLength : int = 10
for X in range(0, ArrayLength):
    for Y in range(0, ArrayLength - 1):
        for Z in range(0, ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z+1]:
                TempValue = ArrayData[X][Z] 
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue

print()
output_array()


def BinarySearch(SearchArray, Lower, Upper, SearchValue) -> int:
    if Upper > Lower:
        Mid = int((Lower + (Upper-1)) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1

for _ in range(2): print(BinarySearch(ArrayData, 0, 10, int(input("Enter search value: "))))

