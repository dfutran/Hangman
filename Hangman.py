#David Futran
#Last Modified: 04/30/15
#Hangman


def getWord(diction):
    #this will import a word to use
    from random import randint
    return diction[randint(0,19)]
def getGuess(wordList):
    #this function will only return the guess if it is valid. Must be single letter not yet used
    guess = input("Guess a Letter: ")
    if guess in tried:
        print ("you tried this already")
        return ''
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
        print ("That is not a letter, you can not trick me!")
        return ''
    elif len(guess) != 1:
        print ("Enter a SINGLE letter. thank you")
        return ''
    else: return guess
def findAll(str, ch):
    #this will find all the charachters in a string, and return them
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i+1
            

diction = ('hello','tower','watchman','rabbit','coconut','spanish','watermelon','surprise','glasses','apartment','computer','kitchen','castle','sleep','school','baseball','snowboard','teacher','succeed','giraffe')
tried = ''
correct = ''
lives = 6
win = False
print("Lets Play Hangman!")
choice = getWord(diction)
a = len(choice)
print ("The word you must guess has ",a," letters in it")


while(lives>0):#The game will repeat until the player runs out of lives
    guess = getGuess(tried)
    
    #first test if a valid guess was entered, if not then repeat the loop so the user can enter a new one
    if not guess:
        continue

    #next if the guess is in the word, print out where. also check if the user found all the letters
    elif guess in choice:
        print ("Correct!")
        print ("It appears in the following location(s) of the word ",list (findAll(choice,guess)),"\n")
        a-=1
        correct = correct + guess
        tried = tried + guess
        over = True
        for i in range(len(choice)):
            if choice[i] not in correct:
                over = False
                break
        if over:
            win = True
            lives=0

    #lastly, if the guess was a valid type, but not correct, then subtract 1 from lives        
    else:
        print ("nope")
        tried = tried + guess
        lives-=1
        print("You have ",lives," lives left, try again\n")

#At the end of the loop print out the right message based on the boolean win       
if win:
    print ("Yay! you won! the word is " + choice)
else:
    print ("sorry, you lost, the word is " + choice)


