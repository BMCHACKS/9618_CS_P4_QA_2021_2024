

def SortDescending():
    ArrayLength = len(Animals)
    for x in range(0, ArrayLength):
        for y in range(0, ArrayLength-x-1):
            if Animals[y] < Animals[y+1]:
                Temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = Temp

# main

global Animals # array 10 elements string

Animals = [
    "horse", "lion", "rabbit", "mouse", "bird",
    "deer", "whale", "elephant", "kangroo", "tiger"
]

SortDescending()

for animal in Animals: print(animal)
