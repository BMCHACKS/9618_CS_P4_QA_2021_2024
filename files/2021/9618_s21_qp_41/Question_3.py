
class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question # DECLARE PRIVATE question : STRING
        self.__answer = answer # DECLARE PRIVATE answer : INTEGER
        self.__points = points # DECLARE PRIVATE points : INTEGER
    
    def getQuestion(self): return self.__question
    def checkAnswer(self, v): return self.__answer == v
    def getPoints(self, v):
        match v:
            case 1 : return self.__points
            case 2 : return self.__points // 2
            case 3 | 4 : return self.__points // 4
        return 0


def readData():
    try:
        file = open('TreasureChestData.txt', 'r')
        for line in file:
            question = line.rstrip()
            answer = file.readline().rstrip()
            points = file.readline().rstrip()
            arrayTreasure.append(TreasureChest(question, int(answer), int(points)))
    except IOError:
        print("[ERROR] File Not Found")

# main

arrayTreasure = []
readData()  

while True:
    question_pos = int(input("Enter a question number [1-5]: "))
    if question_pos >= 1 and question_pos <= 5: break
    print("[ERROR] Question MUST be [1-5], try again...")

question_pos -= 1
attempts = 0
question = arrayTreasure[question_pos].getQuestion()

while True:
    print(f"Q. {question}")
    attempts += 1
    answer = int(input("Enter answer: "))
    if arrayTreasure[question_pos].checkAnswer(answer):
        print("[GOOD JOB] Answer is correct!")
        break
    else:
        print("[WRONG] Answer is incorrect!")
    
points = arrayTreasure[question_pos].getPoints(attempts)
print(f"You get {points} points!")

