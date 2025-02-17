
def Enqueue(to_add):
    global tail_pointer, head_pointer
    if tail_pointer == 100: return False

    if head_pointer == -1: head_pointer = 0
    Queue[tail_pointer] = to_add
    tail_pointer += 1
    
    return True

def IterativeOutput(start, total):
    if start < head_pointer: return total  
    return IterativeOutput(start-1, total+Queue[start])

# main

Queue = [0 for _ in range(100)]
head_pointer = -1
tail_pointer = 0

success, failed = 0, 0
for number in range(1, 21):
    response = Enqueue(number)
    if response:
        success += 1
    else:
        failed += 1

if success == 20: 
    print("Successful")
else:
    print("Unsuccessful")


totaled = IterativeOutput(tail_pointer, 0)
print(totaled)
