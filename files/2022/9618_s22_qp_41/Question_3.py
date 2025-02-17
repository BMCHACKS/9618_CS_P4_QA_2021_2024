def Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, DataToAdd):
    if NumberItems == 10:
        return (False, QueueArray, HeadPointer, TailPointer, NumberItems)
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumberItems += 1
    return (True, QueueArray, HeadPointer, TailPointer, NumberItems)

def Dequeue(Queue, HeadPointer, TailPointer, NumberItems):
    if NumberItems == 0:
        return ("FALSE", Queue, HeadPointer, TailPointer, NumberItems)
    return_value = QueueArray[HeadPointer]
    HeadPointer += 1
    NumberItems -= 1
    if HeadPointer == 10: HeadPointer = 0 
    if NumberItems == 0: HeadPointer, TailPointer = 0, 0
    return (return_value, Queue, HeadPointer, TailPointer, NumberItems)

# main
QueueArray = ["" for _ in range(10)] # [0:9] OF STRING
HeadPointer, TailPointer, NumberItems = 0, 0, 0 # : INTEGER

for _ in range(11):
    value = input("Enter: ")
    returned_val, QueueArray, HeadPointer, TailPointer, NumberItems = Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, value)
    if returned_val:
        print("Data Added!")
    else:
        print("Queue is Full!")

for _ in range(2):
    returned_val, QueueArray, HeadPointer, TailPointer, NumberItems = Dequeue(QueueArray, HeadPointer, TailPointer, NumberItems) 
    print(returned_val)
