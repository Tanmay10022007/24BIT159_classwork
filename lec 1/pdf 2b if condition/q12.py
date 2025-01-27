#12

x=float(input("x coordinate of center"))
y=float(input("y coordinate of center"))
r=float(input("radius of circle"))
x1=float(input("x coordinatwe of  the given point"))
y1=float(input("y coordinate of the given point"))
f=(x-x1)**2 + (y-y1)**2 - (r)**2
if(f<0):
    print("point lies inside circle")
elif(f==0):
    print("point lies on the circumference of circle")
else:
    print("point lies outside circle")
            