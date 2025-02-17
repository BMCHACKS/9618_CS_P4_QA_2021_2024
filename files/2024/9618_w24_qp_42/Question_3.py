
def ReadData():
    try:
        file = open("HighScoreTable.txt", 'r')
        index = 0
        for line in file:
            player_id = line.rstrip()
            game_lvl = file.readline().rstrip()
            score = file.readline().rstrip()
            HighScores[index] = [player_id, game_lvl, score]
            index += 1        
    except IOError:
        print("[ERROR] File Not Found!")


def OutputHighScores(array):
    for x in range(len(array)): print(f"{array[x][0]} reached level {array[x][1]} with a score of {array[x][2]}")


def SortSorces(array):
    for x in range(len(array)):
        swap = False
        for y in range(len(array)-1-x):
            if array[y][2] < array[y+1][2]: array[y], array[y+1] = array[y+1], array[y]
            swap = True
        if not swap: break
    return array


# main

HighScores = [["", "", ""] for _ in range(7)]

ReadData()
print("Before")
OutputHighScores(HighScores)
SortSorces(HighScores)
print("After")
OutputHighScores(HighScores)
