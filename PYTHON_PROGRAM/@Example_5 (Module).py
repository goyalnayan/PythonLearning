# What is the correct syntax of printing all variables and function names of the "mymodule" module?
# print(dir(mymodule))


print("\nMODULE_UD.............")
print('\n')
import MODULE_UD
MODULE_UD.main()  # this is running two time that's why we used if __name__ == "__main__":


# Note: When using a function from a module, use the syntax: module_name.function_name.
import MODULE_UD
print(MODULE_UD.sum(10, 20))
print(MODULE_UD.mul(10, 20))
import MODULE_UD as m   # m is alias (this help us to short module name)
print(m.sum(10, 20))
print(m.mul(10, 20))
from MODULE_UD import *  # in this type of module you can directly call as many function as many you want easily
print(sum(10, 20))
print(mul(10, 20))
from MODULE_UD import sum  # in this type of module you can directly call whatever function you want easily
print(sum(10, 20))
from MODULE_UD import mul  # in this type of module you can directly call whatever function you want easily
print(mul(10, 20))

# Import the module named mymodule, and call the greeting function:
import MODULE_UD
MODULE_UD.greetings("Nayan")

import MODULE_UD
a = MODULE_UD.person1['name']
print(a)
from MODULE_UD import person1
print(person1["age"])

from MODULE_UD import keywords
print(keywords())

print("\nMATH MODULES.............")
from math import *
print(floor(4.5))
print(ceil(4.5))
print(factorial(5))
print(sqrt(49))
print(pow(5, 2))

import math
print(math.ceil(23.2))
print(math.floor(23.2))
print(math.fabs(-23.2))  # it will return the absolute of a given number
print(math.fsum([1, 2.5, 3]))  # this is a list
print(math.gcd(23, 56))
print(math.lcm(12, 56))
print(math.exp(1))
print(math.exp(2))
print(math.log(10, 2))  # 10 to the power base 2
print(math.log(5, 5))
print(math.pow(2, 3))  # 2 to the power of 3
print(math.sqrt(144))
print(math.sin(10))
print(math.sinh(10))  # hyperbolic sin() function
print(math.degrees(1.57))  # convert radian to degree
print(math.radians(90))  # convert degree to radian
print(math.pi)
print(math.e)
print(math.tau)


print('\n')
# Write a Python program to configure the rounding to round up and round down a given decimal value. Use decimal.Decimal
import decimal
print("Configure the rounding to round up:")
decimal.getcontext().prec = 1
decimal.getcontext().rounding = decimal.ROUND_UP
print(decimal.Decimal(30) / decimal.Decimal(4))
print("Configure the rounding to round down:")
decimal.getcontext().prec = 3
decimal.getcontext().rounding = decimal.ROUND_DOWN
print(decimal.Decimal(30) / decimal.Decimal(4))
print("Configure the rounding to round up:")
print(decimal.Decimal('8.325').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_UP))
print("Configure the rounding to round down:")
print(decimal.Decimal('8.325').quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))

print('\n')
import decimal
print("Configure the rounding to round to the floor:")
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_FLOOR  # Use decimal.ROUND_FLOOR
print(decimal.Decimal(20) / decimal.Decimal(6))
print("Configure the rounding to round to the ceiling:")
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_CEILING  # Use decimal.ROUND_CEILING
print(decimal.Decimal(20) / decimal.Decimal(6))


print("\nBuilt-in MODULES.............")
# import this
# print(this)

import keyword
print(keyword.kwlist)  # find list of keyword

# help() function is used to display the documentation of modules, functions, classes, keywords etc.
# help('keywords')
# help('modules')
# help("symbols")
# help("str")
# help("!=")
# help('math')
# help()  # write directly in console

import platform
print(platform.system())
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform
print(dir(platform))

print('\n')
import os
print(os.getcwd())  # cwd- get current working directory

# OS Module needs to be installed to delete any file. After installing the module, os.remove() function is used to delete a file.
# import os
# os.remove("ChangedFile.csv")
# print("File Removed!")

print('\n')
# Write a Python program to get the Python version you are using.
import sys
print("python version", sys.version)
print("version info", sys.version_info)

print("\nIMPORT DATE/ TIME MODULE............")
import calendar
print(calendar.month(2023, 4))
# The epoch is the point where the time starts, the return value of time.gmtime(0) .
# It is January 1, 1970, 00:00:00 (UTC) on all platforms.

import time
stobj = time.localtime()
print(stobj)
print(stobj.tm_mday, end="/")  # module 'time' has no attribute like these 'tm_mday' so, don't use time.tm_mday
print(stobj.tm_mon, end="/")
print(stobj.tm_year)
print(stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print(stobj.tm_sec)

print('\n')
print(time.time())  # timestamp
print(time.ctime())  # this function is used to get current date and time

# print('Hello')
# print(time.sleep(1))
# print('World')

print('\n')  # Write a program to convert from yyyy-mm-dd format to dd-mm-yyyy format.
import datetime
new_date = datetime.datetime.strptime("2023-04-06", '%Y-%m-%d').strftime('%d-%m-%Y')
print(new_date)
from datetime import datetime
new_date = datetime.strptime("2023-04-06", '%Y-%m-%d').strftime('%d-%m-%Y')  # Y should be capital
print(new_date)

print('\n')  # Write a Python program to display the current date and time.
import datetime
x = datetime.datetime.now()
print(x)
print(x.date())
print(x.time())
print(x.year, end="/")
print(x.month, end="/")
print(x.day)
print(x.strftime("%d, %B, %Y, %A"))  # %A represent weeks name and %B represent month "full name"
print(x.strftime("%Y-%m-%d %H:%M:%S"))
x = datetime.datetime(2022, 12, 30, 23, 15, 47)
print(x)  # creating Date objects
print(x.date())
print(x.time())


print("\nRANDOM MODULE.......")
import random
import string
print(random.choice(string.ascii_letters))  # Generate a random alphabetical character
max_length = 10
str1 = ""  # Generate a random alphabetical string
for i in range(random.randint(1, max_length)):
    str1 = str1 + random.choice(string.ascii_letters)
print(str1)
str1 = ""  # Generate a random alphabetical string of a fixed length
for i in range(10):
    str1 = str1 + random.choice(string.ascii_letters)
print(str1)


list1 = ["Star Plus", "DD1", "Zee-tV", "AajTak", "CodeWithHarry"]
print(random.choice(list1))
random.shuffle(list1)
print(list1)

print("\n")  # The random module has a set of methods
print(random.randint(12, 17))
print(random.randint(0, 10) * 7)  # Generate a random multiple of 7 between 0 and 70
print(random.randrange(10, 234))
print("Generate a float between 0 and 1, excluding 1:")
print(random.random())  # Random.random() takes no arguments. It will print anything from 0.0 to 1.0
print(random.random() * 100)  # but if you want to print random number till 100 so, you can ,multiply it with 100

print("\n")
print("Set a random seed and get a random number between 0 and 1:")
random.seed(10)  # you will always get same as the first random number.
print(random.random())
print(random.Random().random())  # random number
print(random.Random(0).random())  # seeded random number

# print('\n')
# print("Generate a random color hex: ", end="")
# print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
# random_number = random.randint(0, 16777215)
# hex_number = str(hex(random_number))
# hex_number ='#' + hex_number[2:]
# print('A Random Hex Color Code is :', hex_number)

print("\nshallow-copy and deepcopy......................")
# Deep copy and Shallow Copy
'''
Syntax: copy.deepcopy(x)
Syntax: copy.copy(x)  # shallow-copy
'''


list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
list2 = list1
list2[1][2] = 4
print('old list:', list1, id(list1))  # old list also changed with new list and ids are same of both list
# If we make any changes in any value in list1 or list2, the change will reflect in both.
print('new list:', list2, id(list2))

import copy
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
z = copy.deepcopy(x)
print(x)
x[2][2] = 'Hello'  # we made chance in the list1 that not reflected in the other list.
print(x)


print('\n')  # deep copy
import copy
dict1 = ["a", "b", "c", "d"]
dict2 = copy.copy(dict1)  # shallow copy
dict3 = copy.deepcopy(dict1)  # deep copy
# As you can see that both have the same value but have different IDs.
print("dict2 ID", id(dict2), "value", dict2)
print("dict3 ID", id(dict3), "value", dict3)
dict1.append("e")
print(dict1)
dict1.clear()
print(dict1)


print('\n')  # we made chance in the list1 that not reflected in the other list.
import copy
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = copy.copy(list1)  # shallow copy
list1.append([13, 14, 15])
print("Old list:", id(list1), list1)
print("New list:", id(list2), list2)

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
z = copy.deepcopy(x)  # deep copy
x.append([13, 14, 15])
print("Old list:", id(x), x)
print("New list:", id(z), x)


print('\n')  # shallow copy
# importing copy for copy operation
import copy
# initializing list 1
list1 = [1, 2, [3, 5], 8]

# using copy to shallow copy
list2 = copy.copy(list1)

# original elements of list
print("The original elements before shallow copying")
for i in range(0, len(list1)):
    print(list1[i], end=" ")

print("\r")  # adding and element to new list
list2[2][0] = 10
# we made chance in the list1 that reflected in the other list.

# checking if change is reflected
print("The original elements after shallow copying")
for i in range(0, len(list1)):
    print(list1[i], end=" ")


print('\n')  # deep copy
import copy
list1 = [1, 2, [3, 5], 4]  # initializing list1
list2 = copy.deepcopy(list1)  # using copy to shallow copy
print("The original elements before deep copying")
for i in range(0, len(list1)):
   print(list1[i], end=" ")
print("\r")
# adding and element to new list
list2[2][0] = 7
# change is reflected in list2
print("The new list of elements after deep copying ")
for i in range(0, len(list1)):
    print(list2[i], end=" ")
print("\r")
# change is not reflected in original list as it is a deep copy
print("The original elements after deep copying")
for i in range(0, len(list1)):
   print(list1[i], end=" ")


print('\nRequest Modules............')
import requests
x = requests.get('https://www.w3schools.com/python/module_requests.asp')
print(x.text)


print("\nEuclidean distance......................")  # Calculate Distance Between Two Points ( Co-ordinates)
from math import sqrt
x1 = 4
y1 = 8
x2 = 5
y2 = 1
formula = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(formula)
formula = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(formula)

print('\n')
from math import sqrt
class eculdn_dstanc:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def formula(self):
        formula_dis = sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)  # don't forget to sue self
        print(formula_dis)
d = eculdn_dstanc(4, 8, 5, 1)
# d = euclidean_dist(x1=4, y1=8, y2=5, x2=1)  # keyword argument
d.formula()

print('\n')  # Calculate Euclidean distance
import math  # Example points in 3-dimensional space...
from math import dist
x = (5, 6, 7)
y = (8, 9, 9)
print(math.dist(x, y))
print(dist(x, y))

print('\n')
p = [3, 3]  # p[0]/x1 = 3, p[1]/y1 = 3
q = [6, 12]  # q[0]/x2 = 6, q[1]/y2 = 12
formula = ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2) ** 0.5  # this is the math term  ((x2 -x1)**2 + (y2-y1)**2) ** 0.5
print(formula)

import math
p = [3, 3]
q = [6, 12]
formula = math.sqrt(
    (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)  # this is the math term  math.sqrt((x2 -x1)**2 + (y2-y1)**2)
print(formula)

print('\n')
import math
p = [3, 3]
q = [6, 12]
formula = math.sqrt(
    (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)  # this is the python term  math.sqrt((x1 -x2)**2 + (y1-y2)**2)
print(formula)

import math  # Example points in 2-dimensions...
p = [3, 3]
q = [6, 12]
print(math.dist(p, q))

import numpy as np
p = [3, 3]
q = [6, 12]
euclidean_dist = np.sqrt(((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2))
print(euclidean_dist)