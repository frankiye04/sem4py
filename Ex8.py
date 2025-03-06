import numpy as np
array = np.array([[5, 8, 1],
 [3, 7, 9],
 [4, 6, 2]])
print("2D Array:")
print(array)
row_sum = np.sum(array, axis=1)
row_min = np.min(array, axis=1)
row_max = np.max(array, axis=1)
col_sum = np.sum(array, axis=0)
col_min = np.min(array, axis=0)
col_max = np.max(array, axis=0)
print("\nRow-wise Results:")
print("Sum of rows:", row_sum)
print("Minimum of rows:", row_min)
print("Maximum of rows:", row_max)
print("\nColumn-wise Results:")
print("Sum of columns:", col_sum)
print("Minimum of columns:", col_min)
print("Maximum of columns:", col_max)