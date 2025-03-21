# Creating Dictionary 1
dict1 = {}
n1 = int(input("How many entries for Dictionary 1? "))
for i in range(n1):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    dict1[key] = value

# Creating Dictionary 2
dict2 = {}
n2 = int(input("\nHow many entries for Dictionary 2? "))
for i in range(n2):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    dict2[key] = value

# Creating Dictionary 3
dict3 = {}
n3 = int(input("\nHow many entries for Dictionary 3? "))
for i in range(n3):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    dict3[key] = value

# Printing the dictionaries
print("\nDictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)
Ans = { ** dict1, ** dict2, **dict3 }
print(Ans)