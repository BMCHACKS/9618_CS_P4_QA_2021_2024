
def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]

        FreeNode += 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode

def PrintAll():
    for x in range(len(ArrayNodes)):
        print(f"{ArrayNodes[x][0]} {ArrayNodes[x][1]} {ArrayNodes[x][2]}")

def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1: InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][2] != -1: InOrder(ArrayNodes, ArrayNodes[RootNode][2]) 

# main

ArrayNodes = [[0,0,0] for x in range(20)] # DECLARE ArrayNodes : [0:19, 0:2] OF INTEGER
RootPointer = -1 # DECLARE RootPointer : INTEGER
FreeNode = 0 # DECLARE FreeNode : INTEGER

for _ in range(10): 
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)
    PrintAll()


InOrder(ArrayNodes, RootPointer)
