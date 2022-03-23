
def powerofnumber(num,power):
    res=1
    while power>0:
        if power%2!=0:
            res=res*num
        num=num*num
        power=power//2
    return res

num=int(input("Enter number"))
power=int(input("Enter Power"))
print(powerofnumber(num,power))
