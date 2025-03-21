s=set()
x=int(input("enter number of values to add in set"))
for i in range(x):
    ele=input("enter the element :")
    s.add(ele)
a=set()
b=set()
for i in s:
    if(i[0]=="A"or i[0]=="a"):
        a.add(i)
    elif(i[0]=="B"or i[0]=="b"):
        b.add(i)
    else:
        pass

print(a,b)