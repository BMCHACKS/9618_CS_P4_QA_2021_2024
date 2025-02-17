
def ReadHighScores():
    try:
        file = open("HighScore.txt", 'r')
        for x in range(10):
            Players[x][0] = file.readline().rstrip()
            Players[x][1] = int(file.readline().rstrip())
        file.close()
    except IOError:
        print("File Not Found!")

def OutputHighScores(): 
    for name, score in Players: print(f"{name} {score}")

def SetList(name, score):
    Players.append([name, score])
    if score > Players[9][1]:
        for i in range(1, len(Players)):
            key = Players[i]
            j = i - 1
            while j >= 0 and Players[j][1] < key[1]:
                Players[j+1] = Players[j]
                j -= 1
            Players[j+1] = key
    return Players

def WriteTopTen():
    try:
        file = open("NewHighScore.txt", "w")
        for x in range(10): file.write(Players[x][0] + '\n'); file.write(str(Players[x][1]) + '\n')
    except IOError:
        print("File Error!")

# main

Players = [["", 0] for _ in range(10)]

ReadHighScores(); OutputHighScores()

name = input("Enter Player Name (3-characters): ")

while True:
    score = int(input("Enter Score: "))
    if score >= 1 and score <= 100_000: break
    print("Score MUST be between 1 - 100000")

Players = SetList(name, score)
OutputHighScores()

WriteTopTen()