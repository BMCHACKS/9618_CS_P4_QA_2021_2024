def IterativeCalculate(Number):
    ToFind = Number
    Total = 0
    while Number != 0:
        if ToFind % Number == 0:
            Total += Number
        Number -= 1
    return Total


def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveValue(Number - 1, ToFind)
        else:
            return RecursiveValue(Number - 1, ToFind)

value = IterativeCalculate(10)
print(value)

value = RecursiveValue(50, 50)
print(value)
