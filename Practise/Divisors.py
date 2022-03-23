
def printdivisors(num):
    i=1
    while((i*i)<=num):
        if((num%i)==0):
            print(i)
            if(i!=num//i):
                print(num//i)
        i+=1

num=int(input("Enter Number \n:"))
printdivisors(num)
