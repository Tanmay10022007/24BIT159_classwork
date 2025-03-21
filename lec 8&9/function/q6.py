def func1():
    li=[]
    n=int(input("give the ending number"))
    for i in range(1,n+1):
        t=(i,i**2,i**3)
        p=tuple(t)
        li.append(p)
    return li    
li= func1()
print(li)