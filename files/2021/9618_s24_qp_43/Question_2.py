class Tree:
    # self.__TreeName : STRING
    # self.__HeightGrowth : INTEGER
    # self.__MaxHeight : INTEGER
    # self.__MaxWidth : INTEGER
    # self.__Evergreen : STRING
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName
        self.__HeightGrowth = HeightGrowth
        self.__MaxHeight = MaxHeight
        self.__MaxWidth = MaxWidth
        self.__Evergreen = Evergreen

    def GetTreeName(self): return self.__TreeName 
    def GetGrowth(self): return self.__HeightGrowth 
    def GetMaxHeight(self): return self.__MaxHeight
    def GetMaxWidth(self): return self.__MaxWidth
    def GetEvergreen(self): return self.__Evergreen 
    

def ReadData():
    TreeArray = []
    try:
        file = open("Trees.txt", 'r')
        for text in file:
            TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen = text.rstrip().split(',')
            TreeArray.append(Tree(TreeName, int(HeightGrowth), int(MaxHeight), int(MaxWidth), Evergreen))
        file.close()
    except IOError:
        print("[ERROR] File not found!")
    return TreeArray

def PrintTrees(TreeObj):
    TreeName, HeightGrowth, MaxHeight = TreeObj.GetTreeName(), TreeObj.GetGrowth(), TreeObj.GetMaxHeight()
    MaxWidth, Evergreen = TreeObj.GetMaxWidth(), TreeObj.GetEvergreen()

    if Evergreen == 'Yes':
        print(f"{TreeName} has a maximum height {MaxHeight} a maximum width {MaxWidth} and grows {HeightGrowth} cm a year. It does not lose its leaves.")
    else:
        print(f"{TreeName} has a maximum height {MaxHeight} a maximum width {MaxWidth} and grows {HeightGrowth} cm a year. It loses its leaves each year.")


def ChooseTrees(TreeObj):
    print("- - ENTER THE REQUIREMENTS OF THE TREE - -")
    Valid_Trees = []
    MaxHeight = int(input("Enter the Max Height: "))
    MaxWidth = int(input("Enter the Max Width: "))
    Evergreen = input("Evergreen or not? [Yes, No]: ")
    for tree in Trees:
        if tree.GetMaxHeight() <= MaxHeight and tree.GetMaxWidth() <= MaxWidth and tree.GetEvergreen() == Evergreen:
            Valid_Trees.append(tree)
    for tree in Valid_Trees:
        PrintTrees(tree)

    tree_name = input("Enter the name of the Tree that you prefer: ")
    tree_height = int(input("Enter the height of the Tree: "))
    for x in range(len(Valid_Trees)):
        if Valid_Trees[x].GetTreeName() == tree_name:
            print(f"The tree will take {(Valid_Trees[x].GetMaxHeight() - tree_height) / Valid_Trees[x].GetGrowth()} years to reach the height of {Valid_Trees[x].GetMaxHeight()}")
            break

# main
Trees = ReadData()
PrintTrees(Trees[0])
ChooseTrees(Trees)
