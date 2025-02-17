WordsArray = []
NumberWords = -1

def ReadWords(file_name):
    global NumberWords
    file = open(file_name, 'r')
    for word in file:
        WordsArray.append(word.rstrip())
        NumberWords += 1
    Play()

def Play():
    global NumberWords
    
    print(f"The main word is: {WordsArray[0]}")
    print(f"Number of possible answers: {NumberWords}")
    print("Enter 'no' to stop.")

    WordsArray[0] = 'null'
    correct_answers = 0
    guess = ""
    
    while guess != 'no':
        guess = input("Enter your ans: ")
        added = False
        for x in range(len(WordsArray)):
            if WordsArray[x] == guess:
                WordsArray[x], added = "null", True
                correct_answers += 1
                break
        
        print("Correct!") if added else print("Incorrect!") 
    
    print()
    print(f"You scored: {int(correct_answers/NumberWords * 100)}%")
    print("<<<< You did not enter these words! >>>>", '\n')
    for word in WordsArray:
        if word != "null": print(word)



# main
which_file = input("Enter 'easy', 'medium' or 'hard' to pick the difficulty: ")
match which_file:
    case 'easy' : ReadWords('Easy.txt')
    case 'medium' : ReadWords('Medium.txt')
    case 'hard' : ReadWords('Hard.txt')

