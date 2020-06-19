"""
Pseudorandom Number Generator
"""
import random

def middle_picker(num):
    num=str(num)
    num=num[1:]
    num=num[:-1]
    num=int(num)
    return num

def make4(num):
    num=str(num)
    while len(num)<4:
        num=num+"0"
    num=int(num)
    return num

def updiv(num,num2):
    numtem=num/num2
    numtem2=round(numtem)
    if numtem2<numtem:
        numtem2+=1
    return numtem2


while True:
    a=int(input("What length number do you want? "))
    seed=int(str(random.randint(0,9))+str(random.randint(0,9)))
    times=updiv(a,4)
    bignum=""
    double=0
    for x in range (times):
        big=seed**2
        big=make4(big)
        if big==double:
            seed=int(str(random.randint(0,9))+str(random.randint(0,9)))
        else:
            double=big
            bignum+=str(big)
            seed=middle_picker(big)
            if seed==0:
                seed=int(str(random.randint(0,9))+str(random.randint(0,9)))
    while len(bignum)>a:
        bignum=bignum[:-1]
    print(bignum)
    again=input("again? ")
    again=again.lower()
    if not again=="y" or again=="yes":
        break
