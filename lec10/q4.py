def palindrome_str(s):
    if type(s)==str:
        return s==s[::-1]
    else:
        return False
lst=['madam','python',"malayalam",12321]
l=list(filter(palindrome_str,lst))
print(l)