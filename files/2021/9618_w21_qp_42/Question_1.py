
def Unknown(x, y):
    if x < y:
        print(x+y)
        return (Unknown(x+1, y)*2)
    else:
        if x == y:
            return 1
        else:
            print(x+y)
            return (Unknown(x-1, y)//2)

def IterativeUnknown(x, y): 
    total = 1
    while x != y:
        print(x+y)
        if x < y: x += 1; total *= 2 
        if x > y: x -= 1; total //= 2
    return total

# main
print(Unknown(10, 15))
print(Unknown(10, 10))
print(Unknown(15, 10))

print("ITERATIVE UNKNOWN")
print(IterativeUnknown(10,15))
print(IterativeUnknown(10,10))
print(IterativeUnknown(15,10))
