import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the elements row by row:")
array = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != cols:
        print(f"Error: Row {i+1} must have exactly {cols} elements.")
        exit(1)
    array.append(row)

array_np = np.array(array)

search_element = int(input("Enter the element to search for: "))
result = np.where(array_np == search_element)
if result[0].size > 0:
    print(f"Element {search_element} found at the following positions (row, column):")
    for r, c in zip(result[0], result[1]):
        print(f"({r}, {c})")
else:
    print(f"Element {search_element} not found in the array.")

search_element = int(input("Enter the element to search for: "))
result = np.where(array_np == search_element)
if result[0].size > 0:
    print(f"Element {search_element} found at the following positions (row, column):")
    for r, c in zip(result[0], result[1]):
        print(f"({r}, {c})")
else:
    print(f"Element {search_element} not found in the array.")
