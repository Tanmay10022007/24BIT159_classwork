lst=[(),("tanmay"),("159")]
for i in lst:
    if type(i)==tuple and len(i)==0:
        lst.remove(i)
print(lst)        