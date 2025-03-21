def sum_avg():
    sum=0
    n=int(input("enter the number of subjects "))
    for i in range(n):
        marks=int(input("enter marks obtained"))
        sum+=marks
    avg=float(sum/n)
   
    return sum,avg
sum,avg =sum_avg()
print(sum,avg)