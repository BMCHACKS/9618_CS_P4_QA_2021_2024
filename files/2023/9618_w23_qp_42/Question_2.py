def IterativeCalculate(Number : int) -> int:
    ToFind = Number
    Total = 0
    while Number != 0:
        if ToFind % Number == 0:
            Total += Number
        Number -= 1
    return Total


value = IterativeCalculate(10)
print(value)

value = IterativeCalculate(4)
print(value)
value = IterativeCalculate(100)
print(value)


