import random
random=[]
for i in range(30):
    random.append(random.randint(-10,20))
print("20 random numbers are",random)
positive = []
negative = []
for num in random:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print("Positive numbers are",positive)
print("Negative numbers are",negative)