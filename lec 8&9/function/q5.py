def ispangram(s:str):
   
   set1=set(s.lower())
   alphast='qwertyuiopasdfghjklzxcvbnm'
   alphaset=set(alphast)
   for s in alphaset:
            if set(s) <= set1:
                pass
            else:
                return False
   return True
a=ispangram("The quick brown fox jumps over the lazy dog himv")
print(a)
b=ispangram("Crazy Fredrick bought many very exquisite opal jewels")



