"""
ELIZA

Description: a virtual therapist
"""
"""
LESSON: 2.5 - Randomness & Libraries
EXERCISE: Virtual Friend
"""
import random

r1="I see. Tell me more."
r2="I'm not quite sure what you mean. Can you elaborate on that?"
r3="And how does that make you feel?"
r4="Please go on"
r5="Why do you want"
r6="Goodbye."
r7="Hello!"
r8="You already said that. Why did you say that again?"
print("I am ELIZA, the artificial therapist.")
print("Type 'goodbye' at any time to end our conversation.")
print("What's bothering you?")

rlist=""

r=""
while not r.lower()=="goodbye":
    r=input()
    iw= r.split( )
    r=r.lower()
    

    if r.endswith("."):
        r=r.replace(".","")
    if r.endswith("!"):
        r=r.replace("!","")
    if not rlist.find(r)==(-1):
        rc=8
    elif iw[0].lower()=="i" and iw[1].lower()=="want" and r.find(" but ")==(-1) :
        rc=5
        r=r.replace("i want ","")
    elif iw[0].lower()=="i" and iw[1].lower()=="want":
        rc=3
    elif r.lower()=="goodbye":
        rc=6
    elif iw[0].lower()=="hello":
        rc=7
    else:
        rc=random.randint(1,4)
    if rc==1:
        print (r1)

    elif rc==2:
        print (r2)

    elif rc==3:
        print (r3)
    
    elif rc==4:
        print (r4)

    elif rc==5:
        print (r5,r+"?")
    
    elif rc==6:
        print (r6)
        
    elif rc==7:
        print (r7)
        
    elif rc==8:
        print (r8)
        
    rlist=(rlist+" "+r)
