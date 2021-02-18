import random

def Guess(x):
    randomNumber=random.randint(1,x)
    guess=0
    tries=3
    while guess!=randomNumber and tries>0:
        guess=int(input(f'Guess a number between 1 and {x}:\n'))
        tries-=1
        if tries>1:
            print(f"You have {tries} tries left")
        elif tries==1 and guess!=randomNumber:
            print("You have one try left!")
    if guess==randomNumber:
        print(f"You guessed the number {randomNumber}!")
    elif tries==0:
        print("You lost!")

#delete "#" to try out
#Guess(10)

def computerGuess(x):
    lowBound=1
    highBound=x
    feedback=""
    while feedback!="c":
        guess=random.randint(lowBound,highBound)
        feedback=input(f"Is {guess} too low(L), too high(H) or correct(C)?\n").lower()
        if feedback=="l":
            lowBound=guess+1
        elif feedback=="h":
            highBound=guess-1

    print(f"Your number is {guess}!")

#delete "#" to try out
x=int(input("Your number is between 1 and: "))
computerGuess(x)
