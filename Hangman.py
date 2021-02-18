from words import words
import random
import string

def GetValidWord(words):
    word=random.choice(words)
    while "-" in word or " " in word:
        word=random.choice(words)
    word=word.upper()
    return word

def Hangman():
    word=GetValidWord(words)
    wordLetters=set(word) # letters in word
    alphabet=set(string.ascii_uppercase)
    usedLetters=set() # what the user guessed

    lives=6

    #getting user input
    while len(wordLetters)>0 and lives>0:
        print(f"You have {lives} lives left.\nYou have used these letters: "," ".join(usedLetters))
        # " ".join() ["a","b","cd"] --> a b cd (string)
        userLetter=input("Guess a letter: ").upper()

        #what the current word is
        wordList=[letter if letter in usedLetters else "-" for letter in word]
        print("Current word: "," ".join(wordList))
        
        if userLetter in alphabet-usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives-=1
                print(f"{userLetter} is not in the word")
        elif userLetter in usedLetters:
            print("You have already used that letter.\n")
        else:
            print("Invalid character.\n")
        #print("Current word: ", " ".join(wordList))
    if lives==0:
        print(f"You died. The word was {word}")
    else:
        print(f"You have guessed the word, {word}")


Hangman()