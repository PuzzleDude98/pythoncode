"""
no0b_text

Description:
"""
import random
while True:
    text=input("Input text to no0b-ify: ")
    r=random.randint(0,11)
    arbitrary=0
    text+=" lol"
    while True:
        text+="ol"
        arbitrary+=1
        if arbitrary==r:
            break
    text2=""
    for char in text:
        if char.isalpha():
            if char=="o":
                r=random.choice([1,2])
                if r==1:
                    y="0"
            r=random.choice([1,2])
            if r==1:
                y=char.upper()
            else:
                    y=char.lower()
        else:
            y=char
        y=str(y)
        text2+=y
    print(text2)
    out=input("Type 1 to no0b-ify another text ")
    if not out=="1":
        break
