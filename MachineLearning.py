"""
Machine_Learning

Description: Use basic machine learning to make a comprehensible sentence
"""
import random
#word_list2=["the","small","cute","rubber","duckies","will","go","to","war","soon"]

"""
pos1=random.choice(word_list)
pos2=random.choice(word_list)
pos3=random.choice(word_list)
pos4=random.choice(word_list)
pos5=random.choice(word_list)
pos6=random.choice(word_list)
pos7=random.choice(word_list)
pos8=random.choice(word_list)
pos9=random.choice(word_list)
pos10=random.choice(word_list)
"""

"""
while True:
    word=random.choice(word_list)
    print(word)
    cute=input("Cute? ")
    if cute=="y":
        word_list.append(word)
    elif cute=="stop":
        break
"""
print("Welcome to the machine learning program!")
print("Say if each word is a boys word!(y/n)")
tr=input("Enter the amount of training data to automate")
nos=[]
word_list=["cute","adorable","baby","kitten","love","war","rage","guns","tanks","explosions"]

print("AUTOMATED TRAINING DATA")
print("~~~~~~~~~~~~~~~~~~~~~~~")
print()
for x in range(tr):
    num=random.randint(0,(len(word_list)-1))
    word=word_list[num]
    print(word)
    if word=="cute" or word=="adorable" or word=="baby" or word=="kitten" or word=="love":
        cute="y"
    else:
        cute="n"
    print("Cute?",cute)
    if cute=="y":
        word_list.append(word)
    elif cute=="n":
        nos.append(word)
    if nos.count(word)>=10:
        nos.remove(word)
        word_list.remove(word)

print()
print()
print()
print("HUMAN TRAINING DATA:")
print()
while True:
    print()
    word=random.choice(word_list)
    print(word)
    cute=input("Cute? ")
    if cute=="y":
        word_list.append(word)
    elif cute=="stop":
        break
