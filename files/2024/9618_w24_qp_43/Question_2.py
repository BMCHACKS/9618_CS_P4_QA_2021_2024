
class Horse:
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        # PRIVATE self.__Name : STRING
        # PRIVATE self.__MaxFenceHeight : MaxFenceHeight
        # PRIVATE self.__PercentageSuccess : PercentageSuccess
        self.__Name = Name
        self.__MaxFenceHeight = MaxFenceHeight
        self.__PercentageSuccess = PercentageSuccess
    
    def GetName(self): return self.__Name
    def GetNaxFenceHeight(self): return self.__MaxFenceHeight
    def Success(self, fence_height, fence_risk):
        if fence_height > self.__MaxFenceHeight: success = 20/100 * self.__PercentageSuccess
        elif fence_height <= self.__MaxFenceHeight:
            match fence_risk:
                case 5 : success = 0.6 * self.__PercentageSuccess   
                case 4 : success = 0.7 * self.__PercentageSuccess
                case 3 : success = 0.8 * self.__PercentageSuccess 
                case 2 : success = 0.9 * self.__PercentageSuccess 
                case 1 : success = 1.0 * self.__PercentageSuccess 
        return round(success, 2)

class Fence:
    # PRIVATE self.__Height : INTEGER
    # PRIVATE self.__Risk : INTEGER
    def __init__(self, Height, Risk):
        self.__Height = Height
        self.__Risk = Risk

    def GetHeight(self): return self.__Height
    def GetRisk(self): return self.__Risk

# main

Horses = [Horse('Beauty', 150, 72), Horse('Jet', 160, 65)]
print(len(Horses))
print(Horses[0].GetName())
print(Horses[1].GetName())


Course = []


for _ in range(4):
    while True:
        height = int(input("Enter Height (70-180 cm): "))
        risk = int(input("Enter Risk (1-5): "))
        if (height >= 70 and height <= 180) and (risk >= 1 and risk <= 5): 
            Course.append(Fence(height, risk))
            break
        print("[ERROR] Height and Risk must follow their criterias!")


scores = []
for y in range(len(Horses)):
    avg = 0
    for x in range(len(Course)):
        height, risk = Course[x].GetHeight(), Course[x].GetRisk()
        val = Horses[y].Success(height, risk)
        avg += val
        print(f"The Horse {Horses[y].GetName()} at fence {x+1} has a chance {val}% of success")
    scores.append(avg)
    print(f"The Horse {Horses[y].GetName()} has an average {avg//4}% chance of jumping over all four fences")
    print()

print()
if scores[0] > scores[1]: print(f"{Horses[0].GetName()} has greater average chance of success!")
else: print(f"{Horses[1].GetName()} has greater average chance of success!")
