global StackVowel
global StackConsonant

StackVowel = ["" for _ in range(100)] # ARRAY[0:99] OF CHAR
StackConsonant = ["" for _ in range(100)] # ARRAY[0:99] OF CHAR

VowelTop = 0 # INTERGER
ConsonantTop = 0 # INTERGER

def PushData(char) -> None:
    global VowelTop, ConsonantTop
    if char in "aeiou":
        if VowelTop == 100:
            print("StackVowel is full!")
        else:
            StackVowel[VowelTop] = char 
            VowelTop += 1
    else: 
        if ConsonantTop == 100:
            print("StackConsonant is full!")
        else:
            StackConsonant[ConsonantTop] = char 
            ConsonantTop += 1

def ReadData() -> None:
    try:
        file = open('StackData.txt', 'r')
        for char in file:
            PushData(char.rstrip())
    except IOError:
        print("File doest not exist!")

def PopVowel() -> str:
    global VowelTop
    if VowelTop == 0: return "No data"
    VowelTop -= 1
    return StackVowel[VowelTop]

def PopConsonant() -> str:
    global ConsonantTop
    if ConsonantTop == 0: return "No data"
    ConsonantTop -= 1
    return StackConsonant[ConsonantTop]


# main
ReadData()
final_string = ""
for _ in range(5):
    choice = input("vowel or consonant?: ")
    if choice == 'vowel':
        rv = PopVowel()
        if rv == "No data": print("VowelStack is empty!")
        final_string += (rv if rv != "No data" else "")
    else:
        rv = PopConsonant()
        if rv == "No data": print("ConsonantStack is empty!")
        final_string += (rv if rv != "No data" else "")

print(final_string)

