QueueData = ["null"]*20
QueueHead = -1 
QueueTail = -1

def Enqueue(data_to_insert):
    global QueueTail, QueueHead
    if QueueTail != 19:
        QueueTail += 1
        if QueueHead == -1: 
            QueueHead = 0
        QueueData[QueueTail] = data_to_insert
        return True
    return False

def Dequeue():
    global QueueTail, QueueHead
    if QueueHead == -1:
        return "false"
    return_value = QueueData[QueueHead]
    QueueHead += 1
    if QueueHead > QueueTail: 
        QueueHead = -1 
        QueueTail = -1
    return return_value


def StoreItems():
    invalid_total = 0
    for _ in range(10):
        check_sum = 0
        user_string = list(input("Enter a 7 character stirng: "))
        check_digit = int(user_string[-1]) if user_string[-1] != 'X' else int(10)
        user_string.pop()
        user_string_sum = [int(user_string[x])*3 + int(user_string[x-1]) for x in range(1, len(user_string), 2)]
        for values in user_string_sum: check_sum += values
        check_sum //= 10
        if check_sum == check_digit:
            if Enqueue(''.join(user_string)):
                print("Value has been enqued!")
            else:
                print("Queue if full!")
        else:
            print("Invalid value!")
            invalid_total += 1
    print(f"Total invalid: {invalid_total}")

    
# main      
StoreItems()
response = Dequeue()
if response == "false":
    print("The Queue is empty!")
else:
    print(response)
