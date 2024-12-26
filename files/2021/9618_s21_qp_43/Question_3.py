class TreasureChest:
    # DECLARE questions : STRING
    # DECLARE answer : INTEGER
    # DECLARE points : INTEGER
    def __init__(self, q, a, p):
        self.__question = q
        self.__answer = a
        self.__points = p

    def getQuestion(self) -> str: return self.__question
    def checkAnswer(self, val) -> bool: return val == self.__answer
    def getPoints(self, val) -> int: 
        p = self.__points
        return p if val == 1 else (p//2 if val == 2 else (p//4 if val == 3 or val == 4 else 0))



arrayTreasure = []
def readData():
    try:
        file = open("TreasureChestData.txt", 'r')
        for line in file:
            q = line.rstrip()
            a = int(file.readline().rstrip())
            p = int(file.readline().rstrip())
            arrayTreasure.append(TreasureChest(q, a, p))
    except IOError:
        print("File not found!")

# main 

readData()
response = int(input("Enter a question number from (1 - 5): "))
print(f'Q{response}. {arrayTreasure[response-1].getQuestion()}')
answer = int(input("ANS: "))
attempts = 1
while not arrayTreasure[response-1].checkAnswer(answer):
    print("ANSWER IS WORNG! TRY AGAIN")
    answer = int(input("ANS: "))
    attempts += 1

print("Points earned: ", arrayTreasure[response-1].getPoints(attempts))

