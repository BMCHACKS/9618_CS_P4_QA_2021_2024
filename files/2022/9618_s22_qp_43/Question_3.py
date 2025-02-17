
def Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, DataToAdd):
    if NumberItems == 10:
        return QueueArray, HeadPointer, TailPointer, NumberItems, False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumberItems += 1
    return QueueArray, HeadPointer, TailPointer, NumberItems, True

def Dequeue():
    global number_of_items, head_pointer, tail_pointer
    if number_of_items == 0: return False

    data = QueueArray[head_pointer]
    head_pointer += 1
    if head_pointer > 9: head_pointer = 0
    number_of_items -= 1
    if number_of_items == 0: head_pointer, tail_pointer = 0, 0

    return data


# main

QueueArray = ['' for _ in range(10)] # DECLARE QueueArray : ARRAY[0:9] OF STRING
head_pointer = 0 # DECLARE head_pointer : INTEGER
tail_pointer = 0 # DECLARE tail_pointer : INTEGER
number_of_items = 0 # DECLARE number_of_items : INTEGER

for _ in range(11):
    data = input("Enter a character: ")
    QueueArray, head_pointer, tail_pointer, number_of_items, response = Enqueue(QueueArray, head_pointer, tail_pointer, number_of_items, data)

data = Dequeue()
print(f"Deuqued : {data}")

data = Dequeue()
print(f"Deuqued : {data}")
