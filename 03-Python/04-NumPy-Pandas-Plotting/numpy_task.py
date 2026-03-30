# NumPy in Python - Fourth Day
# This file covers array creation, vectorized operations, aggregations, indexing, reshape, and timing vs lists

import time

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

print("\nArray + 5:", arr + 5)
print("Array * 2:", arr * 2)
arr3 = arr + 4

arr2 = np.arange(1, 10).reshape(3, 3)
print("\nArray 2D:\n", arr2)

print("\nsum along rows:", arr2.sum(axis=1))
print("sum along columns:", arr2.sum(axis=0))

print("\nMean:", arr2.mean())
print("Min:", arr2.min())
print("Max:", arr2.max())
print("Std:", arr2.std())

print("\nSecond row:", arr2[1])
print("Last column:", arr2[:, 2])

print("\nReshaped 1*9:\n", arr2.reshape(1, 9))
print("\nReshaped 9*1:\n", arr2.reshape(9, 1))

start = time.time()
list1 = list(range(1000000))
list2 = [x**2 for x in list1]
end = time.time()
print("Time taken:", end - start)

start = time.time()
arr = np.arange(1000000)
arr2 = arr**2
end = time.time()
print("Time taken with NumPy:", end - start)

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
print("a + b:", a + b)
print("a * b:", a * b)
print("(a + b)/2:", (a + b) / 2)

rand_arr = np.random.rand(5, 5)
print("\nRandom array:\n", rand_arr)
print("Mean of rows:", rand_arr.mean(axis=1))
print("Mean of columns:", rand_arr.mean(axis=0))
