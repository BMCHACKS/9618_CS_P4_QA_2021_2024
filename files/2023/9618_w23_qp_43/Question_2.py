

def Enqueue(data):
    global TailPointer, HeadPointer
    if TailPointer == 50:
        print("[ERROR] The Queue is Full!")
    else:
        if HeadPointer == -1: HeadPointer = 0
        Queue[TailPointer] = data
        TailPointer += 1


def Dequeue():
    global TailPointer, HeadPointer
    if HeadPointer == -1: 
        return "Empty"

    data = Queue[HeadPointer]
    HeadPointer += 1
    if HeadPointer == TailPointer: HeadPointer, TailPointer = -1, 0
    return data


def ReadData():
    try:
        file = open("QueueData.txt", 'r')
        for line in file:
            Enqueue(line.rstrip())
    except IOError:
        print("[ERROR] File Not Found!")


class RecordData:
    def __init__(self):
        self.ID = "" # DECLARE PUBLIC ID : STRING
        self.Total = 0  # DECLARE PUBLIC Total : INTEGER

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
    for x in range(NumberRecords): print(f"ID {Records[x].ID} Total {Records[x].Total}")


# main

Queue = [0 for _ in range(50)]
HeadPointer = -1
TailPointer = 0

Records = [RecordData() for _ in range(50)] # DECLARE Records : ARRAY[0:49] OF RecordData
NumberRecords = 0

ReadData()
for _ in range(TailPointer): TotalData()
OutputRecords()
