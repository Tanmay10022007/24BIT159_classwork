st=input("enter any string: ")
a_count = 0
d_count = 0
for char in st:
    if char.isalpha():
        a_count+=1
    else:
        d_count+=1

print("no. of alphabets are", a_count)
print("no of digits are", d_count)      



