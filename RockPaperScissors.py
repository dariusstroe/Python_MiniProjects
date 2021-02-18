import random

def isWin(user,computer):
    # r>s,r<p,s>p
    if(user=="Rock" and computer=="Scissors") or (user=="Paper" and computer=="Rock") or (user=="Scissors" and computer=="Paper"):
        return "You win!"
    else:
        return "You lose!"

def Game():
    choices=["Rock","Paper","Scissors"]
    computerChoice=random.choice(choices)
    userChoice=input("Choose : Rock(R), Paper(P), Scissors(S):\n").lower()

    if userChoice=="r":
        userChoice="Rock"
    elif userChoice=="p":
        userChoice="Paper"
    elif userChoice=="s":
        userChoice="Scissors"

    result=isWin(userChoice,computerChoice)
    print(result)

Game()