# uppercase():
Ans=''
temp=0
main=input("enter your string :")
for char in main:
     if 'a'<= char <='z':
            temp = ord(char)
            temp = temp-32
            Ans = Ans +chr(temp)
     else:
            Ans= Ans + char   
            
print(Ans)
   


# lower case
Ans=''
temp=0
main=input("enter your string :")
for char in main:
     if 'A'<= char <='Z':
            temp = ord(char)
            temp = temp+32
            Ans = Ans +chr(temp)
     else:
            Ans= Ans + char   
            
print(Ans)
