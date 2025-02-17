
def Initialise():
    global NumberOfJobs
    for _ in range(100): Jobs.append([0, 0])
    NumberOfJobs = 0

def AddJob(job_number, priority):
    global NumberOfJobs
    if NumberOfJobs != 100:
        Jobs[NumberOfJobs][0] = job_number
        Jobs[NumberOfJobs][1] = priority
        NumberOfJobs += 1
        print("Added")
    else:
        print("Not added")

def InterstionSrot():
    global NumberOfJobs
    for i in range(1, NumberOfJobs):
        key = Jobs[i]
        j = i - 1
        while j >= 0 and key[1] < Jobs[j][1]:
            Jobs[j+1] = Jobs[j]
            j -= 1
        Jobs[j+1] = key
    

def PrintArray():
    global NumberOfJobs
    for x in range(NumberOfJobs): print(f"{Jobs[x][0]} priority {Jobs[x][1]}")


# main

Jobs = []
NumberOfJobs = -1

Initialise()

AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

InterstionSrot()
PrintArray()
