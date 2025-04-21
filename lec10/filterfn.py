def divby5(n):
    return True if n% 5 == 0 else False

lst1 = ['A','a','P','q','4','7','+','r','E','Z']
f1 = filter(str.isalpha,lst1)
print(list(f1))

lst2 = [5,25,625,44,57,60]
f2 = filter(divby5,lst2)
print(list(f2))

