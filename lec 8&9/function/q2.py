a=int(input("enter the number of digits")) 
def compute(n:int):
    n_str = str(n)
    sum = int(n_str) + int(n_str * 2) + int(n_str * 3) + int(n_str * 4)
    print(sum)
compute(a)    
 