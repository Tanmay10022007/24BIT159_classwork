n=int(input("enter any number"))
x=int(n/2)
for i in range(2,x+1):

    if(n%i==0 ):
        print("given number is composite")
        break
    elif(n==2):
        print("neither prime nor composite")
    elif(n==3):
        print("given number is prime")
else:
    print("given number is prime")
        