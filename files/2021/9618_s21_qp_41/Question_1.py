class node:
    def __init__(self, data, nextNode):
        self.data = data # DECLARE PUBLIC data : INTEGER
        self.nextNode = nextNode # DECLARE PUBLIC nextNode : INTEGER


def outputNodes(linkedlist, startptr):
    curr = startptr
    while curr != -1: 
        print(linkedlist[curr].data); curr = linkedlist[curr].nextNode    

def addNode(linkedlist, startptr, emptyptr):
    global startPointer, emptyList

    if emptyptr == -1: return False

    val = int(input("Enter an integer: "))
    linkedlist[emptyptr].data = val

    if startptr == -1: startptr = emptyptr

    newnode = emptyptr
    emptyptr = linkedlist[emptyptr].nextNode

    curr = startptr
    while linkedlist[curr].nextNode != -1:
        curr = linkedlist[curr].nextNode
    if curr != startptr: linkedlist[curr].nextNode = newnode
    linkedlist[newnode].nextNode = -1
    
    startPointer = startptr
    emptyList = emptyptr
    return True


# main

LinkedList = [
    node(1, 1), node(5, 4), node(6, 7),
    node(7, -1), node(2, 2), node(0, 6), 
    node(0, 8), node(56, 3), node(0, 9), 
    node(0, -1)
]

startPointer = 0
emptyList = 5


outputNodes(LinkedList, startPointer)

response = addNode(LinkedList, startPointer, emptyList)
if response:
    print("[SUCCESS] Value Added To LinkedList")
else:
    print("[ERROR] LinkedList Full!")

print("AFTER")
outputNodes(LinkedList, startPointer)
