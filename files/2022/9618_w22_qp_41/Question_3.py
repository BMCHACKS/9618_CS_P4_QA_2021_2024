ArrayNodes = [[-1, -1, -1] for _ in range(20)]

ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]

FreeNode = 6
RootPointer = 0



def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)

def PostOrder(RootNode):
    if RootNode[0] != -1:
        PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2] != -1:
        PostOrder(ArrayNodes[RootNode[2]])
    print(str(RootNode[1]))

PostOrder(ArrayNodes[RootPointer])
 