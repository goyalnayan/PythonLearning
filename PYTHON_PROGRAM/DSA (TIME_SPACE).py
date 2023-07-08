# to measure time efficiency using import time
"""
this is not the correct way to measure time
because companies do not use this method
"""

import time
start = time.time()
for i in range(1, 101):
    print(i)
print(time.time()-start)


import time
start = time.time()
i = 1
while i < 101:
    print(i)
    i = i + 1
print(time.time()-start)

# to measure time using counting operations
"""
# F = (c*1.8) + 32
# C = (f-32) * 5/9
"""

def c_to_f(c):
    return c * 9.0 / 5 + 32  # three operations are happening in this program
print(c_to_f(52))

def mysum(x):

    """ one operation is happening outside """
    total = 0  # one operation is here

    """ two operations are happening inside for loop """
    for i in range(x+1):   # one operation is here
        total = total + i   # two operations are here
    return total
print(mysum(6))

""" so you can count the operation this way """
""" 1 + 3x (x in input) """

def search_for_elem(L, e):
    for i in L:
        if i == e:
            return True
    return False
L = [1, 6, 7, 3, 2]
print(search_for_elem(L, 6))









# sum of first n number

print('\n')
# functions
# solution 1
def sumofN(n):
    sum = 0
    # i ----------> 1, 2, 3, 4, 5
    for i in range(1, n+1):
        sum = sum + i
    return sum
# programs
x = sumofN(10)
print(x)


# functions
# solution 2
def sumofN(n):
    return int(n*(n+1)/2)
# programs
x = sumofN(10)
print(x)


print('\n')
# HOW TO FIND THE TIME COMPLEXITY/ANALYSIS OF EXPERIMENTAL STUDY
# we will use time()
from time import time
def sumofN(n):
    sum = 0
    # i ----------> 1, 2, 3, 4, 5
    for i in range(1, n+1):
        sum = sum + i
    return sum
# programs
start_time = time()
x = sumofN(100000000)  # this time is showing 0.0 but as you will increase the input size so time will also increase.
end_time = time()
duration_time = end_time - start_time
print(x)
print(duration_time)


from time import time
def sumofN(n):
    return int(n*(n+1)/2)
# programs
start_time = time()
x = sumofN(12000000677500)  # this is much bigger number than above solution even time is still 0.0
end_time = time()
duration_time = end_time - start_time
print(x)
print(duration_time)

# after executing both solutions we can see solution 2 is taking less time than solution 1


print('\n')
# HOW TO FIND THE SPACE COMPLEXITY/ANALYSIS OF EXPERIMENTAL STUDY
# sum of first n number

# functions
# solution 1
import tracemalloc as tm
def sumofN(n):
    sum = 0
    # i ----------> 1, 2, 3, 4, 5
    for i in range(1, n+1):
        sum = sum + i
    return sum
# programs
tm.start()
x = sumofN(1000000)
print(x)
print(tm.get_traced_memory())
tm.stop()
# (0, 246) "0" is current memory and "246" is the total memory for the program
# we prefer to use functional study not experimental study b/c it takes more time for bigger number to find the space.


# functions
# solution 2
import tracemalloc as tm
def sumofN(n):
    return int(n*(n+1)/2)
# programs
tm.start()
x = sumofN(1000000)
print(x)
print(tm.get_traced_memory())
tm.stop()

