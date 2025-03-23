
def ReadData():
    Temp_Array = []
    Final_Array = [] 
    try:
        Temp_Array = open("HighScoreTable.txt", "r").read().split('\n')    
    except IOError:
        print("[ERROR] File Not Found!")
        
    for x in range(0, len(Temp_Array), 3):
        Final_Array.append([Temp_Array[x], Temp_Array[x+1], Temp_Array[x+2]])
    
    return Final_Array


def OutputHighScores(array):
    for x in range(len(array)):
        print(f"{array[x][0]} reached level {array[x][1]} with a score of {array[x][2]}")


def SortScores(array):
    for x in range(len(array)):
        swap = False
        for y in range(len(array)-1-x):
            if (array[y][1] == array[y+1][1] and array[y][2] < array[y+1][2]) or array[y][1] < array[y+1][1]:
                array[y], array[y+1] = array[y+1], array[y]
                swap = True
        if not swap: break
    return array


# main
HighScores = [["", "", ""] for _ in range(7)]

HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)
