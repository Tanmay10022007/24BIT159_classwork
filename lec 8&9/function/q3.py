def create_array(x, y, z, value):
   
    array = [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]
    return array

array_3d = create_array(3, 4, 5, 7) 

for layer in array_3d:
    for row in layer:
        print(row)
    print()  
