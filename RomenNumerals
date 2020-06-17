"""
RomenNumerals

Description:
A tool to convert base 10 into roman numerals
"""
print("Say 'stop' to stop")
while True:
    x=input("Enter a number with up to 4 digits: ")
    if x=="stop":
        break
    rn=""
    u1=False
    u2=False
    if not x.isdigit or len(x)>4:
        print("well now i am not doing it")
    else:
        n=int(x)
        if n>=9000:
            rn+="MX"
            n-=9000
            u2=True
        if n>=5000:
            rn+="V"
            n-=5000
            u1=True
        if n>=4000:
            rn+="MV"
            n-=4000
            u2=True
        while len(str(n))>3:
            rn+="M"
            n-=1000
        if n>=900:
            rn+="CM"
            n-=900
        if n>=500:
            rn+="D"
            n-=500
        if n>=400:
            rn+="CD"
            n-=400
        while len(str(n))>2:
            rn+="C"
            n-=100
        if n>=90:
            rn+="XC"
            n-=90
        if n>=50:
            rn+="L"
            n-=50
        if n>=40:
            rn+="XL"
            n-=40
        while len(str(n))>1:
            rn+="X"
            n-=10
        if n>=9:
            rn+="IX"
            n-=9
        if n>=5:
            rn+="V"
            n-=5
        if n==4:
            rn+="IV"
            n-=4
        while not n==0:
            rn+="I"
            n-=1
        if u1 and not u2:
            print(" "*26+"_")
        if u2 and not u1:
            print(" "*27+"_")
        if u1 and u2:
            print(" "*26+"__")
        print(x,"in Roman numerals is",rn)
print("Goodbye!")
