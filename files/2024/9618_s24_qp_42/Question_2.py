class Node:
    # DECLARE PRIVATE LeftPointer : INTEGER
    # DECLARE PRIVATE DATA : INTEGER
    # DECLARE PRIVATE RightPointer : INTEGER
    def __init__(self, Data):
        self.__LeftPointer = -1
        self.__Data = Data
        self.__RightPointer = -1

    def GetLeft(self): return self.__LeftPointer
    def GetRight(self): return self.__RightPointer
    def GetData(self): return self.__Data

    def SetLeft(self, v): self.__LeftPointer = v
    def SetRight(self, v): self.__RightPointer = v
    def SetData(self, v): self.__Data = v
    

class TreeClass:
    # DECLARE PRIVATE Tree : ARRAY[0:19] OF NODE
    # DECLARE PRIVATE FirstNode : INTEGER
    # DECLARE PRIVATE NumberNodes : INTEGER
    def __init__(self):
        self.__Tree = [Node(-1) for _ in range(20)]
        self.__FirstNode = -1
        self.__NumberNodes = 0
    
    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            curr = self.__FirstNode
            smaller = True
            while curr != -1:
                prev = curr
                if self.__Tree[curr].GetData() > NewNode.GetData():
                    curr = self.__Tree[curr].GetLeft()
                    smaller = True
                else:
                    curr = self.__Tree[curr].GetRight()
                    smaller = False
            if smaller:
                self.__Tree[prev].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[prev].SetRight(self.__NumberNodes)
            self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0: print("No nodes")
        else:
            for x in range(self.__NumberNodes): print(f"{self.__Tree[x].GetLeft()} {self.__Tree[x].GetData()} {self.__Tree[x].GetRight()}")


# main
TheTree = TreeClass()
for _ in range(7): TheTree.InsertNode(Node(int(input("Enter the value to insert: "))))
TheTree.OutputTree()
