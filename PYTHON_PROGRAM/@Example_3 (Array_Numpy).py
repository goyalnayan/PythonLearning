print("\nARRAY...................")
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# to work with array you have to import a library.
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]  # Access the Elements of an Array
print(x)
cars[0] = 'Toyota'  # Modify the Elements of an Array
print(cars)
x = len(cars)
print(x)
for i in cars:
    print(i)

cars.pop(1)  # Removing Array elements
print(cars)
cars.remove("BMW")
print(cars)

print('\n')
import array as ar
a = ar.array("i", [1, 2, 3, 4])
a.reverse()
print(a)

import array as ar
a = ar.array("i", [1, 3, 5, 7, 9])
a.insert(1, 4)
print(a)

import array as ar
a = ar.array("i", [1, 3, 5, 7, 9])
a.remove(5)
print(a)

import array as ar
a = ar.array("i", [1, 3, 5, 7, 9])
a.pop(2)
print(a)

import array as ar
a = ar.array("i", [1, 3, 5, 7, 9])
a[0] = 2
print(a)

print("\nNumpy...................")
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
arr = np.array(["hello", 1, 2, 3])  # heterogeneous array
print(arr)
print(type(arr))

print('\n')
# How to make numpy array with the help of python objects
myarr = np.array([3, 6, 37, 7], np.int8)
print(myarr)
listarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(listarray)
x = listarray.dtype
print(x)
x = listarray.shape
print(x)
x = listarray.size
print(x)
x = np.array({34, 34, 25, 23, 23, 23})  # it will not take duplicate values
print(x)

print('\n')  # here are some functions in numpy
a = np.zeros((2, 5))
print(a)
x = a.dtype
print(x)
x = a.shape
print(x)
x = a.size
print(x)


print('\n')  # some other functions of numpy
a = np.arange(99)
print("A---", a)
x = a.shape
print("B---", x)
b = a.reshape(3, 33)  # here we will use a. not np.
print("C---", b)
x = b.shape
print("D---", x)
x = b.ravel()  # this will become one dimension
print("E---", x)


print('\n')  # some other functions of numpy
a = np.linspace(1, 5, 4)  # linearly spaced b/w every element
print(a)
a = np.identity(45)
print(a)
x = a.shape
print(x)


print('\nAttribute.....')
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 1, 0]])
print(a)
x = a.sum(axis=0)  # The elements of axis 0 is rows
print(x)
x = a.sum(axis=1)  # The elements of axis 1 is columns
print(x)
x = a.T  # this will change b/t rows and columns
print(x)
x = a.flat
print(x)
for item in a.flat:
    print(item)
x = a.shape
print(x)
x = a.size
print(x)
x = a.nbytes
print(x)


x = a.ndim
print('Dimensions of array:', x)
a = np.array([1, 2, 3, 4], ndmin=6)
x = a.ndim
print('Dimensions of array:', x)

print('\nMethods.....')


print('\nExamples.........')
# How will you reverse the numpy array using one line of code?
arr = np.array([0.21169, 0.61391, 0.0131, 0.16541, 0.5645, 0.5742])
reversed_array = arr[::-1]
print(reversed_array)


# How will you find shape of any given NumPy array?
arr = np.array(['x5', 'x6', 'x7', 'x8'])
shape_array = arr.shape
print(shape_array)

# arr = np.array([('x1', 'x2', 'x3', 'x4'), ('x5', 'x6', 'x7', 'x8')])
arr = np.array([['x1', 'x2', 'x3', 'x4'], ['x5', 'x6', 'x7', 'x8']])
shape_array = arr.shape
print(shape_array)

print('\n')  # You are given a numpy array and a new column as inputs.
# How will you delete the second columns and replace the column with a new column value?
inputArray = np.array([[35, 53, 56], [72, 12, 22], [43, 84, 56]])
new_column = ([20, 30, 40])
# delete 2nd column
arr_del = np.delete(inputArray, 1, axis=1)
print(arr_del)
# insert new_column to array
arr_ins = np.insert(arr_del, 1, new_column, axis=1)
print(arr_ins)


print('\n')  # How will you sort the array
a = np.array([[1, 4], [2, 3]])
x = np.sort(a)
print(x)
x = np.sort(a, axis=1)
print(x)
x = np.sort(a, axis=0)
print(x)
x = np.sort(a, axis=None)
print(x)


print('\nNumpy Quiz\'s--------')
# What is a correct syntax to check the number of dimensions in an array?
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(a.ndim)
a = np.array([[1, 2], [3, 4]], ndmin=6)
print(a.ndim)

# What is a correct syntax to create an array of type float?
a = np.array([1, 2, 3, 4], dtype='f')
print(a)

# What is a correct method to join two or more arrays?
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [9, 1]])
arr3 = np.concatenate((arr1, arr2))
print(arr3)
arr3 = np.concatenate((arr1, arr2), axis=1)
print(arr3)

# What is a correct syntax to mathematically add the numbers of arr1 to the numbers of arr2
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [9, 1]])
arr3 = np.add(arr1, arr2)
print(arr3)

# What is a correct syntax to subtract the numbers from arr1 with the numbers from arr2
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [9, 1]])
arr3 = np.subtract(arr1, arr2)
print(arr3)

print('\n')
# When using the NumPy random module, how can you return a random number from 0 to 100
arr = np.random.rand()
print(arr)
arr = np.random.randint(100)
print(arr)
arr = np.random.randint(100, size=(3, 5))
print(arr)


print('\n')
# Only one of the following statements is true when it comes to Views in NumPy, which one?
""" The view SHOULD be affected by the changes made to the original array. """
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)  # copy is a new array so, it didn't affected on new array (the copy is a new array)


# Only one of the following statements is true when it comes to Copies in NumPy, which one?
""" The copy SHOULD NOT be affected by the changes made to the original array. """
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)  # view is a same array so, it affected on new array (the view is just a view of the original array)


print('\n')
# What is a correct method to split arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)  # at the place of 3 you can use any 'indices_or_sections'
print(newarr)

print('\n')
# What is a correct method to search for a certain value in an array
arr = np.array([1, 2, 3, 4, 5])
x = np.where(arr == 2)  # it will give index number of "2"
print(x)
arr = np.array([1, 2, 3, 4, 5])
x = np.where(arr % 2 == 0)  # it will give odd number based on index number b/c of arr%2==0
print(x)
arr = np.array([1, 2, 3, 4, 5])
x = np.where(arr % 2 == 1)  # it will give odd number based on index number b/c of arr%2==1
print(x)


# What is a correct syntax to return the index of all items that has the value 4 from the array below:
arr = np.array([1, 4, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


# When using the NumPy random module, how can you return a Normal Data Distribution with 1000 numbers,
# concentrated around the number 50, with a standard deviation of 0.2?
"""
random.normal(size=1000, loc=50, scale=0.2)
"""

print('\n')
# What is a correct method to round decimals in NumPy
"""
There are primarily five ways of rounding off decimals in NumPy:
"""
arr = np.trunc([-3.1666, 3.6667])
print(arr)
arr = np.fix([-3.1666, 3.6667])
print(arr)
arr = np.around(3.1666, 2)
print(arr)
arr = np.floor([-3.1666, 3.6667])
print(arr)
arr = np.ceil([-3.1666, 3.6667])
print(arr)
arr = np.ceil([-3.1666, 3.6667])
print(arr)

# What would be the answer of this cumulative summation in NumPy
arr = np.array([1, 2, 3])
print(np.cumsum(arr))
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(np.cumsum(arr))


print('\n')
# Change data type of given numpy array (using astype and dtype)
"""
NumPy uses a character to represent each of the following data types
i = integer
b = boolean
u = unsigned integer
f = float
c = complex float
m = timedelta
M = datetime
O = object
S = string
"""
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr)
print(arr.dtype)
# change the dtype to 'float64'
arr = arr.astype('float64')
print(arr)
print(arr.dtype)

# Insert the correct method to change the data type to integer.
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)

# Insert the correct argument to specify that the array should be of type STRING.
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)

# Insert the correct argument to specify that the array should be of type STRING.
arr = np.array([1, 2, 3, 4], dtype='f')
print(arr)


print('\nNumPy Quiz\'')
# Insert the correct argument for creating a NumPy array with 2 dimensions.
arr = np.array([1, 2, 3, 4], ndmin=2)
print(arr)
# Insert the correct syntax for checking the number of dimension of a NumPy array.
arr = np.array([1, 2, 3, 4])
print(arr.ndim)

# Insert the correct syntax for printing the number 50 from the array.
arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(arr[1, 0])  # don't write like this [1][0]

# Use the correct NumPy method to change the shape of an array from 1-D to 2-D.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Use a correct NumPy method to change the shape of an array from 2-D to 1-D.
arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
newarr = arr.reshape(-1)
print(newarr)

# Use the correct NumPy method to find all items with the value 4.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Use the correct NumPy method to find all items with the value 4.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr % 2 == 0)
print(x)

# Insert the correct slicing syntax to print the following selection of the array:
# Everything from (including) the second item to (not including) the fifth item.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])

# Insert the correct slicing syntax to print the following selection of the array:
# Every other item from (including) the second item to (not including) the fifth item.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4:2])

# Insert the correct slicing syntax to print the following selection of the array:
# Every other item from the entire array.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[::2])
