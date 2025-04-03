def Enqueue(data):
    global QueueHead, QueueTail
    if QueueTail == 19:
        return False

    QueueTail += 1
    QueueData[QueueTail] = data
    if QueueHead == -1:
        QueueHead = 0

    return True

def Dequeue():
    global QueueHead, QueueTail
    if QueueHead == -1:
        return "false"

    return_data = QueueData[QueueHead]
    QueueHead += 1

    if QueueHead > QueueTail:
        QueueHead = -1
        QueueTail = -1

    return return_data

def StoreItems():
    invalid = 0
    for _ in range(10):
        check_string = input("Enter the string to check: ")
        original_digit = check_string[6]
        check_digit = int(check_string[1])*3 + int(check_string[3])*3 + int(check_string[5])*3
        check_digit += int(check_string[0]) + int(check_string[2]) + int(check_string[4])
        check_digit = check_digit // 10
        if check_digit == 10:
            check_digit = "X"

        check_string = check_string[:6] + str(check_digit)

        if check_string[6] == original_digit:
            response = Enqueue(check_string[:6])
            if response:
                print("Data was added successfully!")
            else:
                print("Queue is full!")
        else:
            invalid += 1

    print(f"The number of invalid inputs were: {invalid}")


# main

QueueData = ["" for _ in range(20)]
QueueHead = -1
QueueTail = -1

StoreItems()
response = Dequeue()
if response == "false":
    print("Queue was empty!")
else:
    print(f"Dequeued: {response}")
