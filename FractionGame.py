"""
FractionGame

Description:
"""
import random
import pygame
num=[1,2,3,4,5,6,7,8,9]
den=[1,2,3,4,5,6,8,12,100]
input("Press enter to play")
play=True
while play:
    print("Here we go!")
    r=1
    cs=0
    ps=0
    while True:
        print("Round",(r))
        input("Press enter to begin")
        n=random.choice(num)
        d=random.choice(den)
        if n>d:
            t=n
            n=d
            d=t
        n=str(n)
        d=str(d)
        print("My numerator is",n)
        print("My denominator is",d)
        print("My fraction is",n+"/"+d)
        cf=int(n)/int(d)
        input("Press enter to draw your fractions")
        n=random.choice(num)
        d=random.choice(den)
        if n>d:
            t=n
            n=d
            d=t
        n=str(n)
        d=str(d)
        print("Your numerator is",n)
        print("Your denominator is",d)
        print("Your fraction is",n+"/"+d)
        pf=int(n)/int(d)
        pygame.init()
        
        if pf>cf:
            w="p"
            ps+=1
        elif cf>pf:
            w="c"
            cs+=1
        else:
            w="t"
            r-=1
        g=input("Who won? type p for player, c for me, the computer, or t, if we tied! ")
        if w==g:
            print("Yup! Good job!")
        else:
            print("Ooh, not quite. You should have said",w)
        print("You have",str(ps),"points")
        print("I have",str(cs),"points")
        if w=="t":
            print("We'll just do that round over")
        r+=1
        if r==6:
            break
    if cs>ps:
        print("I win!")
    else:
        print("You win!")
    a=input("Would you like to play again?(y/n) ")
    if a=="y":
        print("Yay!")
    else:
        print("Ok, bye!")
        play=False
