remainingLetterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def Hangman():
    totalWord = []
    numLetters = getNumLetters()
    for i in range(numLetters):
        totalWord.append("_")
    printWord(totalWord)
    guessTillTheEnd(totalWord)

def stripWords(dictionary):
    words = []
    i=0
    for line in dictionary:
        firstSpace = line.find(" ")
        words.append(line[0:firstSpace].lower())
    return words

def vetWords(dictionary, word):
    viableWords = []
    wordLength = len(word)
    for line in dictionary:
        addWord = True
        if (len(line) == wordLength):
            for i in range(wordLength):
                if (word[i] != "_"):
                    if(word[i] != line[i]):
                        addWord = False
                else:
                    if(line[i] not in remainingLetterList):
                        addWord = False
            if (addWord):
                viableWords.append(line)
    #print(viableWords)
    return viableWords

def goodGuess(viableDict):
    if(len(viableDict) == 0):
        print("It doesn't appear that the word you are thinking of is in my dictionary")
        raise SystemExit
    letterDict={}
    for letter in remainingLetterList:
        letterDict[letter] = 0
    for word in viableDict:
        usedLetters = []
        for letter in word:
            if (letter not in usedLetters and letter in remainingLetterList):
                usedLetters.append(letter)
                letterDict[letter]+=1
    return maxFromDict(letterDict)

def maxFromDict(dictionary):
    high = "-1"
    highKey = "-1"
    for key in dictionary:
        if (high == "-1" or dictionary[key] > high):
            highKey = key
            high = dictionary[key]
    print(highKey)
    return highKey
    

def guess(totalWord):
    dictionary = open("Words - A.txt")
    viableDict = []
    viableDict = stripWords(dictionary)
    viableDict = vetWords(viableDict, totalWord)
    guess = goodGuess(viableDict)
    try:
        remainingLetterList.remove(guess)
    except KeyboardInterrupt:
        raise
    except:
        return -1
    print("Guess = '" + guess + "'")
    return guess

def printWord(word):
    for character in word:
        print(character, end=' ')
    print()

def getNumLetters():
    numLetters = input("how many letters are in the word?: ")
    while (not inputIsNum(numLetters)):
        numLetters = input("how many letters are in the word?: ")
    return int(numLetters)

def inputIsNum(humanInput):
    try:
        (int(humanInput))
        return True
    except KeyboardInterrupt:
            raise
    except:
        print("that was not a valid number")
        return False

def letterIsInWord(guess):
    unnacceptableAnswer = True
    answer = ""
    letterInWord = False
    while (unnacceptableAnswer):
        try:
            answer = input("does the letter '" + guess + "' exist in the word (y/n)?: ")
            if (answer == "y" or answer == "n"):
                unnacceptableAnswer = False
                if (answer == "y"):
                    letterInWord = True
            else:
                print("try again, please answer with 'y' or 'n'")
        except KeyboardInterrupt:
            raise
        except:
            return -1
            continue
    return letterInWord

def lettersPositionInWord(guess, attemptNumber):
    if (attemptNumber == 0):
        string = "what is the first place where '" + guess + "' appears in the word? \ninput '0' if there are none: "
    else:
        string = "what is another place where '" + guess + "' appears in the word? \ninput '0' if there are none: "
    position = input(string)
    while (not inputIsNum(position)):
        position = input(string)
    return int(position)

def guessAndPutLetterInWord(totalWord):
    myGuess = guess(totalWord)
    moreWorkLeft = True
    succesfulLetters = 0
    if (not letterIsInWord(myGuess)):
        return succesfulLetters
    while (moreWorkLeft):        
        try:
            position = lettersPositionInWord(myGuess, succesfulLetters)-1
            if (position == -1):
                moreWorkLeft = False
                continue
            totalWord[position] = myGuess
            succesfulLetters+=1
            printWord(totalWord)
        except KeyboardInterrupt:
            raise
        except:
            print("range index not valid")
            continue
    printWord(totalWord)
    return(succesfulLetters)

def guessTillTheEnd(totalWord):
    lettersLeft = len(totalWord)
    triesLeft = 5
    while (lettersLeft > 0 and triesLeft >0):
        letterSuccessStatus = guessAndPutLetterInWord(totalWord)
        if (letterSuccessStatus>0):
            lettersLeft-=letterSuccessStatus
        else:
            triesLeft-=1
            print("Miss, I have " + str(triesLeft) + " tries left!")
            printWord(totalWord)
    gameConclusion(totalWord, lettersLeft, triesLeft)
    return

def gameConclusion(totalWord, lettersLeft, triesLeft):
    if(lettersLeft == 0):
        gameWon(totalWord, triesLeft)
    else:
        gameLost(totalWord, lettersLeft)
    return

def convertListToString(letterList):
    string = ''
    for character in letterList:
        string = string + character
    return string

def gameWon(totalWord, triesLeft):
    print("I win!  the word is '" + convertListToString(totalWord) + "'!  And I still had " + str(triesLeft) + " tries left!")

def gameLost(totalWord, lettersLeft):
    print("I lose!  I ran out of lives!  And I only had " + str(lettersLeft) + " letters left to guess!")
    print("I'll get you next time!!")

Hangman()
