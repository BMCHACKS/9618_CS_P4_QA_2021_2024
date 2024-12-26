class Node:
    def __init__(self) -> None:
        self.data = 0 
        self.nextNode = -1
    
def outputNodes(arr : list, startPointer : int) -> None:
    while startPointer != -1:
        print(arr[startPointer].data)
        startPointer = arr[startPointer].nextNode


def addNode(linkedList : list, startPointer : int, emptyList : int) -> bool:
    if emptyList == -1: return False
    value = int(input("Enter data: "))
    curr = startPointer
    linkedList[emptyList].data = value
    next = linkedList[emptyList].nextNode
    linkedList[emptyList].nextNode = -1
    while curr != -1:
        pev = curr
        curr = linkedList[curr].nextNode
    linkedList[pev].nextNode = emptyList 
    emptyList = next
    return True


# main
startPointer, emptyList = 0, 5

linkedList = [Node() for _ in range(10)]
linkedList[0].data, linkedList[0].nextNode = 1, 1
linkedList[1].data, linkedList[1].nextNode = 5, 4
linkedList[2].data, linkedList[2].nextNode = 6, 7
linkedList[3].data, linkedList[3].nextNode = 7, -1
linkedList[4].data, linkedList[4].nextNode = 2, 2
linkedList[5].data, linkedList[5].nextNode = 0, 6
linkedList[6].data, linkedList[6].nextNode = 0, 8
linkedList[7].data, linkedList[7].nextNode = 56, 3
linkedList[8].data, linkedList[8].nextNode = 0, 9
linkedList[9].data, linkedList[9].nextNode = 0, -1

outputNodes(linkedList, startPointer)
print("BEFORE")
outputNodes(linkedList, startPointer)

print("Value added!") if addNode(linkedList, startPointer, emptyList) else print("Value Not Added!")
print("AFTER")
outputNodes(linkedList, startPointer)
