l=[]
x=int(input("enter the number of words required : "))
for i in range(x):
    word=input("enter the word:")
    l.append(word.upper())  
s=set(l)
print(s)    