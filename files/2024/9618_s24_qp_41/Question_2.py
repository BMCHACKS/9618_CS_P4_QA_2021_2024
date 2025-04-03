class Tree:
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName # PRIVATE DECLARE TreeName : STRING
        self.__HeightGrowth = HeightGrowth # PRIVATE DECLARE HeightGrowth : INTEGER
        self.__MaxHeight = MaxHeight # PRIVATE DECLARE MaxHeight : INTEGER
        self.__MaxWidth = MaxWidth # PRIVATE DECLARE MaxWidth : INTEGER
        self.__Evergreen = Evergreen # PRIVATE DECLARE Evergreen : STRING

    def GetTreeName(self): return self.__TreeName
    def GetGrowth(self): return self.__HeightGrowth
    def GetMaxHeight(self): return self.__MaxHeight
    def GetMaxWidth(self): return self.__MaxWidth
    def GetEvergreen(self): return self.__Evergreen


def ReadData():
    TempTree = [] # Tree
    try:
        file = open("Trees.txt", 'r')
        for line in file:
            name, growth, height, width, green = line.rstrip().split(',')
            TempTree.append(Tree(name, int(growth), int(height), int(width), green))
        file.close()
    except IOError:
        print("File not found!")

    return TempTree


def PrintTrees(TreeObj):
    name = TreeObj.GetTreeName()
    growth = TreeObj.GetGrowth()
    height = TreeObj.GetMaxHeight()
    width = TreeObj.GetMaxWidth()
    eg = TreeObj.GetEvergreen()

    main_msg = f"{name} has a maximum height {height} a maximum width {width} and grows {growth} cm a year."
    if eg == "Yes":
        main_msg = f"{main_msg} It does not lose its leaves."
    else:
        main_msg = f"{main_msg} It loses its leaves each year."

    print(main_msg)


def ChooseTree(TreeArr):
    max_height = int(input("Enter maximum height the tree can be in cm: "))
    max_width = int(input("Enter maximum width the tree can be in cm: "))
    evergreen = input("Enter if the tree should be evergreen or not evergreen (Yes/No): ")

    valid_trees = []
    for TreeObj in TreeArr:
        if TreeObj.GetMaxHeight() <= max_height and TreeObj.GetMaxWidth() <= max_width and TreeObj.GetEvergreen() == evergreen:
            valid_trees.append(TreeObj)

    if len(valid_trees) == 0:
        print("No Tree Matches the Set Requirements!")
    else:
        for TreeObj in valid_trees:
            PrintTrees(TreeObj)

        name = input("Enter the name of one the Trees you would like to buy: ")
        start_height = int(input("Enter the height of the Tree when bought: "))
        for TreeObj in valid_trees:
            if TreeObj.GetTreeName() == name:
                max_height = TreeObj.GetMaxHeight()
                growth = TreeObj.GetGrowth()
        years = (max_height - start_height) / growth
        print(f"The tree will take {years} years to reach its maximum height of {max_height}cm.")

# main

TreeArray = ReadData()
PrintTrees(TreeArray[0])
ChooseTree(TreeArray)
