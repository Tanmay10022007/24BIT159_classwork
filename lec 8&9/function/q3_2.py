def create_array(x, y, z, value):
    array = []  # Initialize an empty list for the 3D array

    for i in range(x):  # Outer loop for the first dimension
        layer = []  # Create a new layer
        for j in range(y):  # Middle loop for the second dimension
            row = []  # Create a new row
            for k in range(z):  # Inner loop for the third dimension
                row.append(value)  # Append the initial value
            layer.append(row)  # Append row to layer
        array.append(layer)  # Append layer to array

    return array  # Return the created 3D array

# Example usage
array_3d = create_array(2, 3, 4, 2)  # 3x4x5 array initialized with 7

# Printing the 3D array
for layer in array_3d:
    for row in layer:
        print(row)
    print()  # Separate layers for clarity
