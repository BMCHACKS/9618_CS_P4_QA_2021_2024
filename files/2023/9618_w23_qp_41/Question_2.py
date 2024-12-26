global Queue
global HeadPointer
global TailPointer
global NumberRecords

Queue = ["" for _ in range(50)]
HeadPointer = -1
TailPointer = 0


def Enqueue(val: str):
    global TailPointer, HeadPointer
    if TailPointer == len(Queue):  print("Queue is full!")
    else:
        Queue[TailPointer] = val
        if HeadPointer == -1: HeadPointer = 0 
        TailPointer += 1 

def Dequeue():
    global HeadPointer, TailPointer
    if HeadPointer == -1: return "Empty"
    value_return = Queue[HeadPointer]
    HeadPointer += 1
    if HeadPointer == TailPointer: HeadPointer, TailPointer = -1, 0
    return value_return


def ReadData():
    try:
        file = open("QueueData.txt", 'r')
        for data in file:
            Enqueue(data.rstrip())
    except IOError:
        print("File does not exist!")

class RecordData:
    def __init__(self):
        self.ID = ""
        self.Total = 0

NumberRecords = 0
Records = [RecordData() for _ in range(50)]


def TotalData():
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

def OutputRecords():
    global NumberRecords
    for x in range(NumberRecords):
        print(f"ID {Records[x].ID} Total {Records[x].Total}")


ReadData()
for _ in range(TailPointer): TotalData()
OutputRecords()
