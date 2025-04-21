def fun():
    print("this function is called by fun()")
def disp():
    print("this function can be called by disp()")
def msg():
    print("this function can be called by msg()")
lst=[fun , disp , msg]
for i in lst:
    i()
