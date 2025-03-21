def convert(s:str):
    
    words = s.split()
    unique=set(words)
    sorted_words=sorted(unique)
    return " ".join(sorted_words)
s=input("enter a string: ")
print(convert(s))