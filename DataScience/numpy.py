# NumPy (Numerical Python) is a library for numerical computing in Python. It provides support for arrays, matrices, and a collection of mathematical functions to operate on these data structures.
import numpy as np

#creating a numpy array
array = np.array([1,2,3,4,5])
print("Array:",array)

#performing operations
mean = np.mean(array)
print("Mean:",mean)

#reshaping an array
reshape_array = array.reshape(5,1)
print("Reshape Array:\n",reshape_array)