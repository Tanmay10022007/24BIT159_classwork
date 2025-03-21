string = []
for num in range(5):
    string.append(input("Enter your string: "))
print("your original string is =",string)
string2 = []
for num in range(5):
    temp =string[num].upper()
    string2.append(temp)
print("your new string is =",string2)

