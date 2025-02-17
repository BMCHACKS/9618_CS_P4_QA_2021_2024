
def InsertData():
    global FirstEmpty, FirstNode
    if FirstEmpty != -1:
        data  = int(input("Enter a number: "))

        LinkedList[FirstEmpty][0] = data
        Current_Node = FirstEmpty

        if FirstNode == -1: 
            FirstNode = FirstEmpty
        else:
            cur = FirstNode
            while LinkedList[cur][1] != -1:
                cur = LinkedList[cur][1]
            LinkedList[cur][1] = Current_Node

        FirstEmpty = LinkedList[Current_Node][1]
        LinkedList[Current_Node][1] = -1


def OutputLinkedList():
    curr = FirstNode
    while curr != -1: 
        print(LinkedList[curr][0])
        curr = LinkedList[curr][1]


def RemoveData(data_to_remove):
    global FirstEmpty, FirstNode
    if FirstNode != -1:
        cur = FirstNode
        while cur != -1 and LinkedList[cur][0] != data_to_remove:
            prev = cur
            cur = LinkedList[cur][1]

        if cur == FirstNode:
            FirstNode = LinkedList[cur][1]
        else:
            LinkedList[prev][1] = LinkedList[cur][1]
        
        LinkedList[cur][1] = FirstEmpty
        FirstEmpty = cur

# main      

LinkedList = [[-1, x+1] for x in range(20)]
LinkedList[19][1] = -1

FirstEmpty, FirstNode = 0, -1

for _ in range(5): InsertData()
OutputLinkedList()
RemoveData(5)
print('After')
OutputLinkedList()
