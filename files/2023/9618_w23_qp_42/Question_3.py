import datetime

class Character:
    def __init__(self, charname, dob, smarts, run):
        self.__CharacterName = charname
        self.__DateOfBirth = dob
        self.__Intelligence = smarts
        self.__Speed = run
    
    def GetIntelligence(self): return self.__Intelligence
    def GetName(self): return self.__CharacterName
    def SetIntelligence(self, val): self.__Intelligence = val
    def Learn(self): self.__Intelligence += (self.__Intelligence*0.1) 
    def ReturnAge(self): return (2023 - self.__DateOfBirth.year)

class MagicCharacter(Character):
    def __init__(self, charname, dob, smarts, run, Element):
        super().__init__(charname, dob, smarts, run)
        self.__Element = Element
    
    def Learn(self):
        current_intelligence = super().GetIntelligence()
        if self.__Element == "Fire" or self.__Element == "Water":
            super().SetIntelligence(current_intelligence + current_intelligence*0.2)
        elif self.__Element == "Earth":
            super().SetIntelligence(current_intelligence + current_intelligence*0.3) 
        else:
            super().SetIntelligence(super().Learn())
    
dob = datetime.date(2019, 1, 1)

FirstCharacter = Character("Royal", dob, 70, 30)
FirstCharacter.Learn()
print(f"The name is: {FirstCharacter.GetName()}, age: {FirstCharacter.ReturnAge()}, he is this much smart {FirstCharacter.GetIntelligence()}")

dob = datetime.date(2018, 3, 3)
FirstMagic = MagicCharacter("Light", dob, 75, 22, "Fire")
FirstMagic.Learn()
print(f"The name is: {FirstMagic.GetName()}, age: {FirstMagic.ReturnAge()}, he is this much smart {FirstMagic.GetIntelligence()}")

