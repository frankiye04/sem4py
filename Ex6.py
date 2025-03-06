import numpy as np
one_d_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
two_d_array = one_d_array.reshape(4, 3)
print("Two-dimensional array:")
print(two_d_array)
print("\nFirst two columns:")
print(two_d_array[:, :2])