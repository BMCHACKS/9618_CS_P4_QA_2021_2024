
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
    if RootNode[0] != -1: PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2] != -1: PostOrder(ArrayNodes[RootNode[2]]) 
    print(RootNode[1])



# main

ArrayNodes = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]

FreeNode = 6
RootPointer = 0

position = SearchValue(RootPointer, 15)
if position == -1:
    print("[NOT FOUND] Value was not found in Tree")
else:
    print(f"[FOUND] Value found at index {position}")

PostOrder(ArrayNodes[RootPointer])

