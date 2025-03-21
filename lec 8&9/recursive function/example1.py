def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        y= n*fact(n-1)
        return y
t=int(input("enter the number whose factorial is needed: ")) 
print(fact(t))