
def InsertData():
    global FirstEmpty, FirstNode
    if FirstEmpty != -1:
        
        data = int(input("Enter a positive integer: "))
        
        LinkedList[FirstEmpty][0] = data
        
        if FirstNode == -1: FirstNode = FirstEmpty

        NewNode = FirstEmpty
        FirstEmpty = LinkedList[FirstEmpty][1]
        
        if FirstNode != -1:
            curr = FirstEmpty
            while LinkedList[curr][1] != -1:
                curr = LinkedList[curr][1]

            LinkedList[curr][1] = NewNode
        LinkedList[NewNode][1] = -1


def OutputLinkedList():
    curr = FirstNode
    while curr != -1:
        print(LinkedList[curr][0])
        curr = LinkedList[curr][1]


def RemoveData(to_remove):
    global FirstEmpty, FirstNode
    if FirstNode != -1:
        curr = FirstNode
        
        while curr != -1 and LinkedList[curr][0] != to_remove:
            prev = curr
            curr = LinkedList[curr][1]
        
        if curr == FirstNode:
            FirstNode = LinkedList[curr][1]  
        else:
            LinkedList[prev][1] = LinkedList[curr][1]
    
        LinkedList[curr][1] = FirstEmpty
        FirstEmpty = curr


# main

LinkedList = [[-1, x+1] for x in range(20)]
LinkedList[19][1] = -1

FirstEmpty = 0
FirstNode = -1


for _ in range(5): InsertData()
OutputLinkedList()

RemoveData(5)
print("After")
OutputLinkedList()
