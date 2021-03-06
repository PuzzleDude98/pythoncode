"""
play21

Description: Play a game of "21" with the user
"""
import random
def userguess(n):
    while True:
        a=input("Will you increment the number by 1, 2, or 3? ")
        try:
            int(a)
        except:
            print("Please try again")
        else:
            if a=="1" or a=="2" or a=="3" and not int(a)+n>21:
                break
            else:
                print("Please try again")
    a=int(a)
    print("The number is now up to",n+a)
    return a

def decide(a,n):
    z=n%4
    if n==20:
        d=1
    elif z==0:
        d=random.randint(1,3)
    else:
        z=n%4
        d=4-z
    n+=d
    print("I choose",d)
    print("The number is now up to",n)
    return n


print("Let's play 21!")
print("Let me explain the rules:")
print("You enter a number between 1 and 3")
print("I add to that number, adding 1, 2, or 3")
print("Then you add to the number, and so on!")
print("If you say 21, you lose!")
print("You cannot add more or less than 1-3, and you cannot go over 21.")
input("Are you ready to play? ")
while True:
    print("Let's play!")
    n=0
    n=decide(0,n)
    while True:
        a=userguess(n)
        n+=a
        if n==20:
            if not n==21:
                w="u"
            else:
                w="c"
            break
        n=decide(a,n)
        if n>=20:
            if not n==21:
                w="c"
            else:
                w="u"
            break
    if w=="u":
        print("Well, I have to choose 1.")
        print("The number is now 21. You win. Good game!")
    else:
        while True:
            a=input("Will you increment the number by 1, 2, or 3? ")
            if a=="2" or a=="3":
                print("That number is over 21, please try again.")
            elif a=="1":
                break
            else:
                print("Please try again")
        print("That brings the number to 21")
        print("You lose")
        print("Good game!")
    r=input("Would you like to play again? (y/n) ")
    if r=="y":
        print("Ok then!")
    else:
        print("Goodbye!")
        break
