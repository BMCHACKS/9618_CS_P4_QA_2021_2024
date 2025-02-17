class Tree:
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        # PRIVATE self.__TreeName : STRING
        # PRIVATE self.__HeightGrowth : INTEGER
        # PRIVATE self.__MaxHeight : INTEGER
        # PRIVATE self.__MaxWidth : INTEGER
        # PRIVATE self.__Evergreen : STRING
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
    Trees = []
    try: 
        file = open("Trees.txt", 'r')
        for line in file:
            name, growth, mheight, mwidth, evergreen = line.rstrip().split(',')
            Trees.append(Tree(name, int(growth), int(mheight), int(mwidth), evergreen))
        return Trees        
    except IOError:
        print("file not found :/")    

def PrintTrees(Treeobj):
    TreeName, MaxHeight, MaxWidth =  Treeobj.GetTreeName(), Treeobj.GetMaxHeight(), Treeobj.GetMaxWidth()
    HeightGrowth, EverGreen = Treeobj.GetGrowth(), Treeobj.GetEvergreen()
    main_msg = f"{TreeName} has a maximum height {MaxHeight} a maximum width {MaxWidth} and grows {HeightGrowth} cm a year."
    if EverGreen == "Yes":
        print(f"{main_msg} It does not lose its leaves.")
    else:
        print(f"{main_msg} It does lose its leaves.")

def ChooseTree(TreeArray):
    NewTreeArray = []
    max_h = int(input("Max Height: "))
    max_w = int(input("Max Width: "))
    egreen = input("Evergreen [Yes|No]: ")
    for tree in TreeArray:
        if tree.GetMaxHeight() <= max_h and tree.GetMaxWidth() <= max_w and tree.GetEvergreen() == egreen: NewTreeArray.append(tree)

    for tree in NewTreeArray: PrintTrees(tree)
    
    name = input("Enter name of Tree to pick: ")
    height = int(input("Enter original height: "))

    for tree in NewTreeArray:
        if name == tree.GetTreeName():
            time = (tree.GetMaxHeight()-height) / tree.GetGrowth()
            print(f"The tree will take {time} years to reach its maximum height of {tree.GetMaxHeight()}")
            break
    

# main

Trees = ReadData()
PrintTrees(Trees[0])

ChooseTree(Trees)