# printing element containing a 
l1=["apple", "banana","papaya","cherry"]
l2=[]
for i in l1:
   if "a" in i:
      l2.append(i)

print(l2) 

# printing element not containing a
l3=[i for i in l1 if 'a' not in i]
print(l3)