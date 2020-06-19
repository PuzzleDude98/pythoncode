"""
Hangman

Description: play a game of "hangman" with the user

Can you find the easter egg and the bug?
"""
import time
input("Press enter to begin")
name=input("What is your name? ")
print ("Hello, " + name, "! Let's play hangman!(WARNING: HARD)")
time.sleep(1)
p2=", your doom!"
print ("Start guessing...")
time.sleep(0.5)
import random
p1="I am "
word = random.choice(["awkward","bagpipes","banjo","bungler","croquet","crypt","dwarves","fervid","fishhook","fjord","gazebo","gypsy","haiku","haphazard","hyphen","ivory","jazzy","jiffy","jinx","jukebox","kayak","kiosk","klutz","memento","mystify","numbskull","ostracize","oxygen","pajama","phlegm","pixel","pizza","polka","quad","quip","rhythmic","rogue","sphinx","squawk","swivel","toady","twelfth","unzip","waxy","wildebeest","yacht","zealous","zigzag","zippy","zombie"])
guesses = ''
turns = 10
pw=(p1+name+p2)
while turns > 0:         
    failed = 0
    for char in word:
        if char in guesses:
            print (char)    
        else:
            print ("_")
            failed += 1
    if failed == 0:        
        print ("You won")
        break
    guess = raw_input("guess a character: ")
    if guess==pw:
        print("I serve you, master. The word is",word)
        guess = raw_input("guess a character: ")
    elif guess=="qwertyuiopasdfghjklzxcvbnm" or guess=="abcdefghijklmnopqrstuvwxyz":
        print("CHEATER!!!!!!")
        turns=1
    guesses += guess                    
    if guess not in word:
        turns -= 1
        print ("Wrong")
        print ("You have", + turns, 'more guesses' )
        if turns == 0:
            print ("You Lose")
            print ("The word was:",word)
