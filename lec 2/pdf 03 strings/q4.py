st1=input("Enter main string")
st2=input("Enter sub string")
"""st3=st1.replace(st2,'')
print(st3)"""
st4=''
for i in range (len(st1)-1):
    if st2 in st1[i]:
        pass
    else:
        st4+=st1[i]

print(st4)        