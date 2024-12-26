arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(value : int) -> bool:
    for x in arrayData:
        if x == value: return True
    return False


# main

val = int(input("Enter a value to search: "))
print(f"Value '{val}' was found!") if linearSearch(val) else print(f"Value '{val}' was NOT found!")


def bubblesort():
    for x in range(10):
        for y in range(9-x):
            if arrayData[y] < arrayData[y+1]: arrayData[y], arrayData[y+1] = arrayData[y+1], arrayData[y] 



