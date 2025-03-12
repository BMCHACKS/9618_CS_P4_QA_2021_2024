
def InsertData():
    global FirstEmpty, FirstNode
    for _ in range(5):
        if FirstEmpty != -1:
            data  = int(input("Enter a number: "))
            NextNode = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = data
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = NextNode


def OutputLinkedList():
    current = FirstNode
    while current != -1:
        print(LinkedList[current][0])
        current = LinkedList[current][1]


def RemoveData(data_to_remove):
    global FirstEmpty, FirstNode
    if FirstNode != -1:
        current = FirstNode
        while current != -1 and LinkedList[current][0] != data_to_remove:
            previous = current
            current = LinkedList[current][1]

        if current == FirstNode:
            FirstNode = LinkedList[current][1]
        else:
            LinkedList[previous][1] = LinkedList[current][1]

        LinkedList[current][1] = FirstEmpty
        FirstEmpty = current

# main      

LinkedList = [[-1, x+1] for x in range(20)]
LinkedList[19][1] = -1

FirstEmpty, FirstNode = 0, -1

InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()
