import random
L=[]
for i in range(20):
    L.append(random.randint(0,100))
print(L)
new=[]
m=int(input("Enter a value"))

position = [index for index, value in enumerate(L) if value == m]

if position:
    print(f"The number {m} is found at position: {position}")
else:
    print(f"The number {m} is not in the list.")