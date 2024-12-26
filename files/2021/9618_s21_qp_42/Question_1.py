
class Node:
    def __init__(self,d:int , n:int):
        self.data = d
        self.nextNode = n


linkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]
startPointer, emptyList = 0, 5


def outputNodes(linkedList, startPointer):
    while startPointer != -1:
        print(linkedList[startPointer].data)
        startPointer = linkedList[startPointer].nextNode


def addNode(linkedList, startPointer, emptyList):
    if startPointer == -1: return False
    value = int(input("Enter value: "))
    linkedList[emptyList].data = value
    curr, next_node = startPointer, emptyList
    while curr != -1:
        pev = curr
        curr = linkedList[curr].nextNode
    linkedList[pev].nextNode = next_node
    emptyList = linkedList[next_node].nextNode
    linkedList[next_node].nextNode = -1
    return True

print("BEFORE")
outputNodes(linkedList, startPointer)

print("Value Added!") if addNode(linkedList, startPointer, emptyList) else print("Linked list is FULL!!")

print("AFTER")
outputNodes(linkedList, startPointer)

