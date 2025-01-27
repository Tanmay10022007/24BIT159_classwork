
print("Enter coordinates of three points:")

x1, y1 = map(float, input("Enter x1 and y1 : "))
x2, y2 = map(float, input("Enter x2 and y2 : "))
x3, y3 = map(float, input("Enter x3 and y3 : "))


if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
    print("The points are collinear.")
else:
    print("The points are not collinear.")
