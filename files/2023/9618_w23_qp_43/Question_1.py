
def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for _ in range(0, LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1
        Value = Value[1: len(Value)]
    return Total


def RecursiveVowels(Value, Total):
    if Value[0] in 'aeiou': 
        Total += 1
        if len(Value) == 1: 
            return Total
    return RecursiveVowels(Value[1:len(Value)], Total)


# main

count = IterativeVowels("house")
print(count)

count = RecursiveVowels("imagine", 0)
print(count)

