import random
s=set()
count=0
while(len(s)<10):

    a= random.randint(15,45)
    if a in s:
        continue
    else:
        s.add(a)

    
print(s)
for j in s.copy():
    if(j<30):
        count+=1
    else :
        pass 

    if(j>35):
        s.discard(j)#discard element greater than 35

print(count)# no of elements less than 30
print(s) 