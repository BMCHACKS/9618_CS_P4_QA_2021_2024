StackData = [""]*10 # : ARRAY[0:9] OF INTEGER
StackPointer = 0 # INTEGER 

def output_stackdata() -> None:
    print(StackPointer)
    for data in StackData: print(data) 


def Push(value : int) -> bool:
    global StackPointer
    if StackPointer == 10: return False
    StackData[StackPointer] = value
    StackPointer += 1
    return True


def Pop() -> int: 
    global StackPointer
    if StackPointer == 0: return -1
    StackPointer -= 1
    value = StackData[StackPointer]
    StackData[StackPointer] = ""
    return value


for _ in range(11):
    value = int(input("Enter a value to push: "))
    response = Push(value)
    if response:
        print("Data has been added!")
    else:
        print("Stack is full!")

output_stackdata()
Pop()
Pop()
output_stackdata()
