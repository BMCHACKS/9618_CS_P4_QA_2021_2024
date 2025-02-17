
def ReadHighScores():
    try:
        file = open('HighScore.txt', 'r')
        for line in file:
            player_name.append(line.rstrip())    
            score.append(int(file.readline().rstrip()))
            
    except IOError:
        print("[ERROR] File Not Found")


def OutputHighScores():
    for x in range(10): print(f"{player_name[x]} {score[x]}")


def add_in_leaderboard(new_name, new_score):
    if new_score > score[9]:
        score.append(new_score)
        player_name.append(new_name)
        for i in range(1, len(score)):
            key = score[i]
            key_name = player_name[i]
            j = i - 1
            while j >= 0 and key > score[j]:
                score[j+1] = score[j]
                player_name[j+1] = player_name[j]
                j -= 1
            score[j+1] = key
            player_name[j+1] = key_name

def WriteTopTen():
    try:
        file = open('NewHighScore.txt', 'w')
        for x in range(10):
            file.write(str(player_name[x]) + '\n')
            file.write(str(score[x]) + '\n')
    except IOError:
        print("[ERROR] File Could Not Be Made")

# main

player_name = []
score = []

ReadHighScores()
OutputHighScores()

while True:
    name = input("Enter your payer name: ")
    your_score = int(input("Enter your score (1-100000): "))
    if len(name) == 3 and (your_score >= 1 and your_score <= 100_000): break
    if len(name) > 3 or len(name) < 3: print("[ERROR] player name must be ONLY 3 Characters" )
    if your_score > 100_000 or your_score < 1: print("[ERROR] Score must be between (1-100000) inclusive" )


add_in_leaderboard(name, your_score)
print("AFTER")
OutputHighScores()
WriteTopTen()
