def count_lower_upper(string:str):
    uppercase=0
    lowercase=0
    for i in string:
        if(i.isupper()):
            uppercase+=1
        else:
            lowercase+=1
    d={f"upper":{uppercase}, "lower":{lowercase}}
    print(d)        
count_lower_upper("Tanmay")