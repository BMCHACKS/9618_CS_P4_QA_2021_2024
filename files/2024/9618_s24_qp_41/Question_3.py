
def Enqueue(data):
    global QueueHead, QueueTail
    if QueueTail != 19:
        if QueueHead == -1: QueueHead = 0
        QueueTail += 1
        QueueData[QueueTail] = data
        return True
    return False

def Dequeue():
    global QueueHead, QueueTail
    if QueueHead == -1: return "false"
    data = QueueData[QueueHead]
    QueueHead += 1
    if QueueHead > QueueTail: QueueHead, QueueTail = -1, -1
    return data

def StoreItems():
    invalid_items = 0
    for _ in range(20):
        val = input("Enter 7-digits: ")
        sum = int(val[0]) + int(val[2]) + int(val[4]) + (int(val[1])*3) + (int(val[3])*3) + (int(val[5])*3)
        check_digit = sum // 10
        val_check_digit = 10 if val[6] == "X" else int(val[6]) 
        if val_check_digit == check_digit:
            val_check_digit = 'X' if val_check_digit == 10 else str(val[6])
            response = Enqueue(val_check_digit)
            match response:
                case False : print("[ERROR] val not added")
                case True : print("[SUCCESS] val added to Queue")
        else:
            print("[ERROR] Check Digit Not Valid!")
            invalid_items += 1
            

# main

QueueData = ["" for _ in range(20)]
QueueHead = -1
QueueTail = -1

StoreItems()
response = Dequeue()
if response == 'false':
    print("The Queue is empty!")
else:
    print(f"Dequeud: {response}")

