import random
import math
from tracemalloc import stop
def try_again():
    lover_value=int(input("small value"))
    uper_value=int(input("big value"))
    a=random.randint(lover_value,uper_value)
    b=math.log(uper_value-lover_value+1,2)
    print(int(b),"chanse you have collected")
    c=1
    
    while c<b:
        d=int(input("enter the guess number"))
        c=c+1
        if d>a:
            print("big number")
        if d<a:
            print("small number")
        if d==a:
            print("you winer")
            stop()

        else:
            print("try again")
    print("this is correct number",a)
    r=input("you continue the game")
    if r=="yes":
                try_again()
    elif r=="no":
                print("ok bay")
try_again()
