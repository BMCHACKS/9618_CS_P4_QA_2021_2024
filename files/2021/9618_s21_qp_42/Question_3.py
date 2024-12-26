
class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    
    def getQuestion(self): return self.__question
    def checkAnswer(self, val): return int(self.__answer) == val
    def getPoints(self, val): 
        full_points = int(self.__points)
        val = (full_points if val == 1 else (full_points // 2 if val == 2 else (full_points // 4 if val == 3 or val == 4 else 0)))
        return val


arrayTreasure = []

def readData():
    try:
        file = open("TreasureChestData.txt", "r")
        for line in file:
            question = line.rstrip()
            answer = file.readline().rstrip()
            points = file.readline().rstrip()
            arrayTreasure.append(TreasureChest(question, answer, points))
        file.close()
    except IOError:
        print("File Not Found")
    
readData()

question_number = int(input("Enter a number (1-5): ")) - 1
ans = int(input(f'{arrayTreasure[question_number].getQuestion()} = '))
attempt = 1
while not arrayTreasure[question_number].checkAnswer(ans):
    print("Answer is WRONG!")
    ans = int(input(f'{arrayTreasure[question_number].getQuestion()} = '))
    attempt += 1

print(f"Points earned: {arrayTreasure[question_number].getPoints(attempt)}")
