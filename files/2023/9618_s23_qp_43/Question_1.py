
def PrintArray(integer_array):
    for data in integer_array: print(data, end=" ")
    print()

def LinearSearch(integer_array, to_find):
    count = 0
    for data in integer_array: 
        if data == to_find: count += 1
    return count


# main

DataArray = []

try:
    file = open("Data.txt", 'r')
    for line in file: DataArray.append(int(line.rstrip()))
except IOError:
    print("[ERROR] File Not Found")

PrintArray(DataArray)


while True:
    number = int(input("Enter a number (0-100) inclusive: "))
    if number >= 0 and number <= 100: break
    print("[ERROR] Number must be in range!")

response = LinearSearch(DataArray, number)
print(f"The number {number} is found {response} times.")

