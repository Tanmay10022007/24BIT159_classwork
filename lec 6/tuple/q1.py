names_list = [("rudra", "tanmay"), "Alice",  ("Rohit",), "kriti"]
print("name are",names_list)
boys = 0
girls = 0
for name in names_list:
    if isinstance(name,tuple):
        boys += len(name)
    elif isinstance(name, str):
        girls += 1

print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")