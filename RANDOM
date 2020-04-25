"""
RANDOM

Description:
"""
import random
a=[]
x=1
print("1. list of random")
print("2. random list of random")
b=int(input("1 or 2?"))
if b==1:
    while x<=75:
        a.append("No")
        x+=1
    x=1
    while x<=25:
        a.append("Yes")
        x+=1
    random.shuffle(a)

elif b==2:
    while x<=100:
        a.append(random.choice(["No", "No", "No", "Yes"]))
        x+=1

a.append("End")
print(str(a.index("End")),"items")
a.remove("End")
x=1
while x<100:
    print(a[x])
    x+=1
