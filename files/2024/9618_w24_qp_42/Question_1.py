class EventItem:
    def __init__(self, EventName, Type, Difficulty):
        self.__EventName = EventName # DECLARE PRIVATE EventName : STRING
        self.__Type = Type # DECLARE PRIVATE Type : STRING
        self.__Difficulty = Difficulty # DECLARE PRIVATE Difficulty : INTEGER 
    
    def GetName(self): return self.__EventName
    def GetEventType(self): return self.__Type
    def GetDifficulty(self): return self.__Difficulty

class Character:
    def __init__(self, CharacterName, Jump, Swim, Run, Drive):
        self.__CharacterName = CharacterName # DECLARE PRIVATE CharacterName : STRING
        self.__Jump = Jump # DECLARE PRIVATE Jump : INTEGER
        self.__Swim = Swim # DECLARE PRIVATE Swim : INTEGER
        self.__Run = Run # DECLARE PRIVATE Run : INTEGER
        self.__Drive = Drive # DECLARE PRIVATE Drive : INTEGER
    
    def GetName(self): return self.__CharacterName

    def CalculateScore(self, event_type, difficulty):
        skill = 0
        match event_type:
            case 'jump' : skill = self.__Jump  
            case 'swim' : skill = self.__Swim 
            case 'run' : skill = self.__Run 
            case 'drive' : skill = self.__Drive
        if skill >= difficulty: return 100

        difference = difficulty - skill

        match difference:
            case 1 : return 80 
            case 2 : return 60 
            case 3 : return 40 
            case 4 : return 20 
        

# main

Group = [
    EventItem('Bridge', 'jump', 3),
    EventItem('Water wade', 'swim', 4),
    EventItem('100 mile run', 'run', 5),
    EventItem('Gridlock', 'drive', 2),
    EventItem('Wall on wall', 'jump', 4)
] 

Character_1 = Character('Tarz', 5, 3, 5, 1)
Character_2 = Character('Geni', 2, 2, 3, 4)


Points_Char_1 = 0
Points_Char_2 = 0

for event in Group:
    event_type, event_difficulty = event.GetEventType(), event.GetDifficulty()
    Chance_Char_1 = Character_1.CalculateScore(event_type, event_difficulty)
    Chance_Char_2 = Character_2.CalculateScore(event_type, event_difficulty)

    if Chance_Char_1 > Chance_Char_2: 
        print(f"{Character_1.GetName()} - Has won the event: {event.GetName()} ")
        Points_Char_1 += 1
    elif Chance_Char_2 > Chance_Char_1: 
        print(f"{Character_2.GetName()} - Has won the event: {event.GetName()} ")
        Points_Char_2 += 1
    else:
        print(f"Event: {event.GetName()} - Has been a DRAW ")

if Points_Char_1 > Points_Char_2:
    print(f"{Character_1.GetName()} - Has won overall with {Points_Char_1} points!")
elif Points_Char_2 > Points_Char_1:
    print(f"{Character_2.GetName()} - Has won overall with {Points_Char_2} points!")
else:
    print("The Event has resulted in a DRAW overall!")

