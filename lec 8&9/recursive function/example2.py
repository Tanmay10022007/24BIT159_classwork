def expo(a,n):
    if(n==0):
        return 1
    else:
        y=a*expo(a,n-1)
        return y
    

t=int(input("enter the value of a: "))
s=int(input("enter the value of n: "))    
print(expo(t,s))



#this is ques 5 too
