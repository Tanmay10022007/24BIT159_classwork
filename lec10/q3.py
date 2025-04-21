import random
lst=[]
for i in  range(0,10):
    lst.append(random.randint(-15,15))

t=list(map(lambda x:x*x,lst))
print(lst,t)
    