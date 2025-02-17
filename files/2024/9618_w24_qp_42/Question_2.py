class Queue:
    def __init__(self, Initial_Data,  HeadPtr, TailPtr):
        self.QueueArray = [Initial_Data for _ in range(100)] # DECLARE PUBLIC QueueArray : INTEGER
        self.Headpointer = HeadPtr # DECLARE PUBLIC HeadPointer : INTEGER
        self.Tailpointer = TailPtr # DECLARE PUBLIC TailPointer : INTEGER

def Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0
        AQueue.Tailpointer += 1
        return 1
    else:
        if AQueue.Tailpointer > 99: 
            return -1
        else:
            AQueue.QueueArray[AQueue.Tailpointer] = TheData
            AQueue.Tailpointer += 1
            return 1

def ReturnAllData():
    ans = ""
    curr = TheQueue.Headpointer
    while curr != TheQueue.Tailpointer:
        ans += f"{str(TheQueue.QueueArray[curr])} "
        curr += 1
    return ans

def Dequeue():
    if TheQueue.Headpointer == -1: return -1

    data = TheQueue.QueueArray[TheQueue.Headpointer]
    TheQueue.Headpointer += 1
    if TheQueue.Headpointer > TheQueue.Tailpointer: 
        TheQueue.Headpointer = -1
        TheQueue.Tailpointer = 0
    return data

# main

TheQueue = Queue(-1, -1, 0)

for _ in range(10):
    while True:
        val = int(input("Enter an integer (greater than 0): "))
        if val >= 0: break
        print("[ERROR] Enter a valid integer!")
    response = Enqueue(TheQueue, val)
    match response:
        case -1 : print("[ERROR] The Queue is full!")
        case _ : print("[SUCCESS] Value Added To Queue!")
    
response = ReturnAllData()
print(response)

for _ in range(2):
    response = Dequeue()
    if response == -1: 
        print("Queue empty")
    else:
        print(response)

response = ReturnAllData()
print(response)
