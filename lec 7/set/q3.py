s=set()
for i in range(5):
    a=input("enter a name :")
    s.add(a)

print(s)    
old=input("enter the number you need modified :")
s.remove(old)
new=input("enter the new number: ")
s.add(new)



del1=input("enter the number you need modified :")
s.remove(del1)


del2=input("enter the number you need modified :")
s.remove(del2)

print(s)