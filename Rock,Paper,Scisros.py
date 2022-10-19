import random
def try_again():
    c=input(" your choice rock paper scisors")
    a=["rock","paper","scisros"]
    b=random.choice(a)
    print(b)
    if b == "paper":
        if c=="paper":
            print("tie")
        elif c== "scisors":
            print("you  winer")
        elif c=="rock":
            print("computer is winer")

    elif b == "rock":
        if c=="rock":
            print("tie")
        elif c== "scisors":
            print("computer is  winer")
        elif c=="paper": 
            print("you winer")

    else:
        b == "scisors"
        if c=="scisors":
            print("tie")
        elif c== "paper":
            print("computer is  winer")
        elif c=="rock":   
            print(" you winer")
        
    r=input("you continue the game")
    if r=="yes":
            try_again()
    elif r=="no":
        print("ok bay")
try_again()









