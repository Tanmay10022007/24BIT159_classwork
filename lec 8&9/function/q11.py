def create_list(list1: list, list2: list):
    
    a=set(list1)
    b=set(list2)

    c=a.intersection(b)
    

    list3=list(c)

    
    
    return list3


list1 = list(map(int, input("Enter space-separated values for list1: ").split()))
list2 = list(map(int, input("Enter space-separated values for list2: ").split()))  
t=create_list(list1, list2)    
print(t)
