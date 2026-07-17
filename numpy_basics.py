import numpy as np
# # Creating Arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

# # Mathematical Operations
print("\nAddition:")
print(arr1 + 5)

print("\nMultiplication:")
print(arr1 * 2)

# # Statistics
print("\nSum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("standard deviation:",np.std(arr1))

# # Reshape
arr3 = np.arange(1, 10).reshape(3, 3)

print("\nReshaped Array:")
print(arr3)

# # Indexing
print("\nFirst Element:", arr1[0])
print("Last Element:", arr1[-1])

# #slicing
print(arr1[1:4])

#sorting
print(np.sort(arr1))

#concanetate
a=np.array([1,15,69,53,8])
b=np.array([4,68,2,75,68])
print(np.concatenate((a,b)))