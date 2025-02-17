
def ReadData():
    local_array = []
    try:
        file = open("Data.txt", 'r')
        for line in file: local_array.append(line.rstrip())
        file.close()
        return local_array
    except IOError:
        print("[ERROR] File not found!")
    
def FormatArray(Array):
    txt = ""
    for data in Array: txt += f"{data} "
    return txt

def CompareString(str_1, str_2):
    for x in range(len(str_1)):
        if str_1[x] < str_2[x]: return 1
        elif str_1[x] > str_2[x]: return 2

def Bubble(Array):
    for x in range(len(Array)):
        swap = False
        for y in range(len(Array)-1-x):
            if CompareString(Array[y], Array[y+1]) == 2:
                Array[y], Array[y+1], swap = Array[y+1], Array[y], True
        if not swap: break
    return Array


# main

main_array = ReadData()
main_string = FormatArray(main_array)

print(main_string)

main_array = Bubble(main_array)
main_string = FormatArray(main_array)

print()
print(main_string)

