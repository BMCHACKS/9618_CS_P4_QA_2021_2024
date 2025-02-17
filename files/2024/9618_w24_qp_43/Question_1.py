
def ReadData():
    local_array = []
    try:
        file = open('Data.txt', 'r')
        for line in file: local_array.append(line.rstrip())
        return local_array
    except IOError:
        print("[ERROR] File Not Found!`")

def FormatArray(string_array):
    concatenated_string = ''
    for data in string_array: concatenated_string += f"{data} "
    return concatenated_string

def CompareStrings(string_1, string_2):
    for x in range(len(string_1)):
        if string_1[x] < string_2[x]: 
            return 1
        elif string_1[x] > string_2[x]: 
            return 2

def Bubble(string_array):
    for x in range(len(string_array)):
        swap = False
        for y in range(len(string_array)-1-x):
            if CompareStrings(string_array[y], string_array[y+1]) == 2:
                string_array[y], string_array[y+1] = string_array[y+1], string_array[y]
                swap = True
        if not swap: break
    return string_array

# main

main_array = ReadData()
main_string = FormatArray(main_array)
print(main_string)


Bubble(main_array)
main_string = FormatArray(main_array)
print(main_string)
