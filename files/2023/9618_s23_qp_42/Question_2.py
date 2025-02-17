

class SaleData:
    def __init__(self, ID, Quantity):
        self.ID = ID # DECLARE PUBLIC ID : STRING
        self.Quantity = Quantity # DECLARE PUBLIC Quantity : INTEGER


def Enqueue(new_record):
    global Head, Tail, NumberOfItems
    if NumberOfItems == 5: return -1
    
    CircularQueue[Tail] = new_record
    Tail += 1
    if Tail > 4: Tail = 0
    NumberOfItems += 1
    return 1


def Dequeue():
    global Head, Tail, NumberOfItems
    if NumberOfItems == 0: return SaleData("", -1)

    data = CircularQueue[Head]
    Head += 1
    if Head > 4: Head = 0
    NumberOfItems -= 1
    if NumberOfItems == 0: Head, Tail = 0, 0

    return data 


def EnterRecord():
    id = input("Enter an id: ")
    qty = int(input("Enter the quantity: "))
    response = Enqueue(SaleData(id, qty))
    
    if response == -1:
        print("Full")
    else:
        print("Stored")
    

# main

CircularQueue = [SaleData("", -1) for _ in range(5)]
Head, Tail, NumberOfItems = 0, 0, 0


for _ in range(6): EnterRecord()

returned_value = Dequeue()

if returned_value.ID == "":
    print("[ERROR] The Queue is empty!")
else:
    print(returned_value.ID)

EnterRecord()

for data in CircularQueue: print(f"{data.ID} {data.Quantity}")

