def IterativeVowels(Value: str) -> int:
    Total, LengthString = 0, len(Value)
    for x in range(0, LengthString):
        FirstCharacter = Value[0]
        if FirstCharacter in 'aeiou':
            Total += 1
        Value = Value[1:len(Value)]
    return Total



def RecursiveVowels(Value: str, Total: int, LengthString: int, MaxLen: int) -> int:
    if LengthString == 0: return Total
    FistCharacter = Value[0]
    if FistCharacter in 'aeiou': Total += 1
    return RecursiveVowels(Value[1:MaxLen], Total, LengthString - 1, MaxLen)


x = 'imagine'
print(IterativeVowels(x))
print(RecursiveVowels(x, 0, len(x), len(x)))

