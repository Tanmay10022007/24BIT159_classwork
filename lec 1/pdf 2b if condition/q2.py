a=int(input("number 1: "))
b=int(input("number 2: "))
c=int(input("number 3: "))
if(a<c and b<c):
    if (a<b):
        print("c is greatest and a is smallest")
    else:
        print("c is the largest and b is smallest")
    
elif(a<b and c<b):
    if(a<c):
        print("b is largest and a is smallest")
    else:
        print("b is largest and c is smallest")

else:
    if(b<c):
        print("a is largest and b is smallest")
    else:
        print("a is largest and c is smallest ")    