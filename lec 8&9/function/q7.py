def ispalindrome(s:str):
    
    t=""
    for elements in s:
        t = elements + t

    
    if(s==t):
        print("the string is a palindrome")
    else:
        print("the string is not an palindrome")    


s=input("enter the string:  ")
ispalindrome(s)




