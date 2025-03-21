def count_alpha_digit(string:str):
    alphabet=0
    digits=0
    for i in string:
        if(i.isalpha()):
            alphabet+=1
        else:
            digits+=1
    d={f"alphabet":{alphabet}, "digit":{digits}}
    print(d)        
count_alpha_digit("Tanmay1002")