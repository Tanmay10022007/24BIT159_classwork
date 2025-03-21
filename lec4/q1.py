import random
odd=random.sample(range(1,100,2),5)
even=random.sample(range(0,100,2),4)

print("list",odd,even)  
odd[2]=even
print(odd)
flattened=[]
for i in odd:
    if type(i)==list:
        for sub in i:
            flattened.append(sub)
    else:
        flattened.append(i)                
flattened.sort()
print(flattened)
