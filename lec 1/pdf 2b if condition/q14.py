marks1=float(input("marks of subject 1 :"))
marks2=float(input("marks of subject 2 :"))
marks3=float(input("marks of subject 3 :"))
Total=marks1+marks2+marks3
Avg=Total/3
print(Total,Avg)

if(marks1<=39 or marks2<=39 or marks3<=39):
    print("FAIL")
else:
    print("PASS")    
if(marks1>80):
    print("grade : O")
elif(70<=marks1<=79):
    print("grade : A+")  
elif(60<=marks1<=69):
    print("grade : A")        
elif(55<=marks1<=59):
    print("grade : B+")        
elif(50<=marks1<=54):
    print("grade : B")        
elif(45<=marks1<=49):
    print("grade : C")        
elif(40<=marks1<=44):
    print("grade : P")   
else:
    print("grade : F")         
      

if(marks2>80):
    print("grade : O")
elif(70<=marks2<=79):
    print("grade : A+")  
elif(60<=marks2<=69):
    print("grade : A")        
elif(55<=marks2<=59):
    print("grade : B+")        
elif(50<=marks2<=54):
    print("grade : B")        
elif(45<=marks2<=49):
    print("grade : C")        
elif(40<=marks2<=44):
    print("grade : P")   
else:
    print("grade : F")        


if(marks3>80):
    print("grade : O")
elif(70<=marks3<=79):
    print("grade : A+")  
elif(60<=marks3<=69):
    print("grade : A")        
elif(55<=marks3<=59):
    print("grade : B+")        
elif(50<=marks3<=54):
    print("grade : B")        
elif(45<=marks3<=49):
    print("grade : C")        
elif(40<=marks3<=44):
    print("grade : P")   
else:
    print("grade : F")                  
