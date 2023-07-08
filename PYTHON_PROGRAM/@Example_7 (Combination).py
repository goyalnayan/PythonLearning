# print('Enter the number')
# n = int(input())
# for i in range(n):
#     print('Hello')
#


print('\n')
a = 'naina'
for i in range(0, len(a)):
    print(a[i], end=" ")  # a[i] will give string one by one
    # print(i, end=" ")  # i will give index
    i = i + 1


print('\n')
capitals = {"USA": "Washigton D.c.", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}
for key in capitals:
    print(key, "->", capitals[key])


print('\n')
chr = 'Nainmackmdsf'
cons = 0
vowel = 0
for c in range(0, len(chr)):  # use range() here
    U_Vowel = ['A', 'E', 'I', 'O', 'U']
    L_Vowel = ['a', 'e', 'i', 'o', 'u']
    if chr[c] in U_Vowel or chr[c] in L_Vowel:
        vowel += 1
    else:
        cons += 1
print("Number of Vowels are ", vowel)
print("Number of consonant are ", cons)


# print('\n')  # Python program to count total string words
# test_string = input("How much string you want to know so, write them in detail : ")
# total = 1
# for i in range(len(test_string)):
#     if test_string[i] == ' ' or test_string == '\n' or test_string == '\t':
#         # if (test_string[i] == '' # (this means we are giving no space so, it means every string word will count as single)
#         total = total + 1
# print("Total Number of Words in our input strings are:", total)

print("\nSlice Operator...............")
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(4)
print(a[x])
x = slice(3, 5)  # use comma for slicing not colon
print(a[x])
x = slice(0, 8, 3)
print(a[x])
str1 = 'good morning'
x = slice(2, 5)
print(str1[x])

print("\nTernary Operator/ Conditional Operator...............")
a, b = 3, 4
c = print("A is greater") if a>b else print("B is greater")


# [if_true] if [expression] else [if_false]
age = 125
discount = 10 if age < 40 else 22
print(discount)

a = 34
b = 234
calculate = 'A' if a > b else 'B'
print(calculate)

a = 34
b = 234
print('A') if a < b else print('B')

a = 330
b = 330
calculate = "A" if a > b else "="
print(calculate)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# here this print("=") is for the if part not for the else part
if a > b:
    print("A")
else:
    if a == b:
        print("=")
    else:
        print("B")

print("\nArithmetic operator (+, -, /, *, %, **, //)....................")
print(4 % 1)  # not 4 but 0
print(4 % 2)  # not 2 but 0
print(24 // 7)  # 3
print(24 // 24)  # not 0 but 1
print(2 // 24)  # 0
print("Logical Operators (and, or, not)....................")
print(False and True)
print(False or True)
print(0 and 1)
print(0 or 1)
print("Bitwise operator (&, |, ^, ~, <<, >>)....................")
print(6 & 3)  # & (AND)
print(6 | 3)  # | (OR)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
"""
print(6 ^ 3)  # ^ (XOR)
"""
8 4 2 1
0 1 1 0
0 0 1 1
0 1 0 1 = 5 (ans)
"""
print(~3)  # Not Bitwise Operator (~0 = 1 and ~1 = 0)
print(3 << 2)  # << (Zero fill left shift)
print(8 >> 2)  # >> (Signed right shift)
print("Assignment Operators (=, +=, -=, *=, %=, **=, //=)....................")
x = 5
x &= 3
print(x)
x = 5
x |= 3
print(x)
x = 5
x ^= 3
print(x)
x = 5
x <<= 3
print(x)
x = 5
x >>= 3
print(x)
print("Comparison/rational Operators (==, !=, <=, >=, >, <)....................")
print("Identity Operators (is, is not)....................")
# "is" compare exact location of an object in memory.
# "==" compare values
a = 4  # 4 is int and int is immutable
b = 4
print(a is b)  # that's why true (int will not change)
print(a == b)

a = [1, 2, 43]  # this is list and list is mutable
b = [1, 2, 43]
print(a is b)  # that's why false (list can be changed)
print(a == b)

a = None
b = None
print(a is b)
print(a is None)
print(a == b)
print('\n')
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # returns True because z is the same object as x
print(x is y)  # returns False because x is not the same object as y, even if they have the same content
print(x == y)  # to demonstrate the difference between "is" and "==": this comparison returns True b/c x is equal to y
print("Membership Operators (in, not in)...................")
x = ["apple", "banana"]
print("banana" in x)  # returns True because a sequence with the value "banana" is in the list
print("pineapple" not in x)  # returns True because a sequence with the value "pineapple" is not in the list


print('\n')  # Python Program to Convert Centimeters to Feet and Inches
""" This is a Python Program to read height in centimeters and then convert the height to feet and inches """
# cm= int(input("Enter the height in centimeters:"))
cm = 50
inches = 0.394 * cm
feet = 0.0328 * cm
print(inches)
print(feet)
print("The length in inches", round(inches, 2))
print("The length in feet", round(feet, 2))

print('\n')  # Python Program to Convert Celsius to Fahrenheit/ Fahrenheit to Celsius
# F = (c*1.8) + 32
# C = (f-32) * 5/9
celsius = 3
Fahrenheit = (celsius * 1.8) + 32
print(Fahrenheit)
F = 64
Celsius = (F - 32) * 5 / 9
print(Celsius)

print('\n')  # Average/ Total
# find the average of list elements
a = [1, 2, 3, 4, 5]
len_a = len(a)
sum = 0
for n in a:
    sum = sum + n
average = sum/len_a
print(average)

print('\n')

# program to accept marks of 5 subjects and find total marks and percentage assuming full marks as 100 in each subject.
x = 75  # float(input("Marks in Math Subject = "))
y = 95  # float(input("Marks in English Subject = "))
z = 72  # float(input("Marks in Science Subject = "))
w = 81  # float(input("Marks in Astronomy Subject = "))
v = 96  # float(input("Marks in Coding Subject = "))
Total = x + y + w + z + v
Average = Total / 5
Percentage = float(Total) * 100 / 500
print("total_marks = ", Total)
print("average_marks = ", Average)
print("percentage_marks = ", Percentage)

print('\n')  # Write a python program to calculate total marks in 5 subjects (Full marks = 100)
a = 78
b = 56
c = 89
d = 90
e = 87
total = a + b + c + d + e
percent = (total / 500) * 100
print("Total Marks=", total, " and Percentage=", percent)
# if elif else statement: To show a multi-way decision based on several conditions, we use if elif else statement
if percent >= 80:
    print("You got A Grade")
elif percent >= 60:
    print("You got B Grade")
elif percent >= 40:
    print("You got C Grade")
else:
    print("You got D Grade")

print('\n')  # Profit/ loss
sp = 400  # float(input("enter selling price:"))
cp = 400  # float(input("enter cost price:"))
if sp > cp:
    print('Profit is ', sp - cp)
elif sp == cp:
    print("No profit, No loss")
else:
    print("Loss is ", cp - sp)

print('\n')  # Calculate Profit for given Selling and Cost Price | profit amount @ 5%
sp = 400  # float(input("enter selling price:"))
cp = 200  # float(input("enter cost price:"))
x = sp - cp
print("Profit is", x)
y = x * 5 / 100
print("5% profit in sale", y)

print('\n')
# Python program to calculate sale price
cp = 600
dis_per = 10
discount = cp * dis_per / 100
print("Discount is ", discount)
sp = cp - discount
print("Selling price is ", sp)

print('\n')  # electricity unit consumption
unit = 1000  # int(input("Enter your electricity unit consumption: "))
payamt = unit * 5  # calculate total price at the rate of Rs. 5/unit
discount = int(payamt) * 10 / 100  # Give a discount of 10% on all over bill.
print("discount is =", discount)

print('\n')
# 1 to 100 units – Rs. 1.5/unit
# 101 to 200 units – Rs. 2.5/unit
# 201 to 300 units – Rs. 4/unit
# 300 to 350 units – Rs. 5/unit
# above 350 -fixed charge 2500/unit
unit = 274  # int(input("Enter the unit consumed: "))
if unit > 0 and unit <= 100:
    payamt = unit * 1.5
    fixedcharge = 25
elif unit > 100 and unit <= 200:
    payamt = (100 * 1.5) + (unit - 100) * 2.5
    fixedcharge = 50
elif unit > 200 and unit <= 300:
    payamt = (100 * 1.5) + (200 - 100) * 2.5 + (unit - 200) * 4
    fixedcharge = 75
elif unit > 300 and unit <= 350:
    payamt = (100 * 1.5) + (200 - 100) * 2.5 + (300 - 200) * 4 + (unit - 300) * 5
    fixedcharge = 100
else:
    payamt = 0
    fixedcharge = 2500
Total = payamt + fixedcharge
print("Electricity bill = %2f" % Total)

print('\n')  # Max of numbers.
def max(a, b):
    if a > b:
        print("A is greater")
        return a
    else:
        print('B is greater')
        return b
print("Maximum is -- ", max(5, 6))

print('\n')
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
def max_of_three(a, b, c):
    return max_of_two(max_of_two(a, b), c)
print(max_of_three(5, -6, 3))

a = 3
b = 15
c = 7
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

print('\n')
a = 5
b = 8
c = 6
d = 3
if a > b:
    print("a is greater than b")
    if c > d:
        print("c is greater than d")
    if d > d:
        print("d is greater than b")
    else:
        print("d is greater than c")
else:
    print("b is greater than a")
    if c > a:
        print("d is greater than b")
    else:
        print("d is greater than c")

print('\n')  # python program to find smallest, greater, and middle number
a = 4
b = 7
c = 3

if a <= b and a <= c:
    print("a is smallest")
elif b <= a and b <= c:
    print("b is smallest")
else:
    print("c is smallest")

if a >= b and a >= c:
    print("a is greatest")
elif b >= a and b >= c:
    print("b is greatest")
else:
    print("c is greatest")

if (a >= b and a <= c) or (a <= b and a >= c):
    print("a is middle number")
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("b is middle number")
else:
    print("c is middle number")

print('\n')  # Python program to calculate are you eligible for voting ot not
age = 25
gender = "Female"
if age >= 18 and (gender == "Female" or "female" or gender == "Male" or "male"):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

print("\n")  # Python Program to Check Whether a given Year is a Leap Year
year = 2024  # int(input("Enter year: "))
if year % 4 == 0:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

# elif (year % 4 ==0) and (year % 100 != 0):

print("\n")  # Positive or negative number find
num = 23
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


print('\n')  # Even/Odd (using list)
def eve_odd(l):
    even = 0
    odd = 0
    for num in l:
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd  # this return will come inside for not inside if/else or even/odd
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(eve_odd(list1))
even, odd = eve_odd(list1)

print('\n')
print(even, odd)
print("even", even)
print("odd", odd)


print('\n')  # print sum of all number that are divisible of 3 and 5
sum = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        sum = sum + i
print(sum)


print("\n")  # prime_composite
n = 17
if n < 0:
    print("Incorrect input")
elif n == 0 or n == 1:
    print("neither 0 nor 1 is a prime or composite number")
elif n > 1:
    for i in range(2, n):
        if n % i == 0:  # use n % i not i % 2 (b/c start value is 2)
            print(n, "is a composite number")
            break
    else:
        print(n, "is a prime number")  # use else part inside for loop
else:
    print("Enter correct input")

n = 171
i = 1
count = 0
while i <= n:
    if n % i == 0:  # use n % i not i % 2 (b/c start value is 2)
        count = count + 1
    i = i + 1
if count == 2:
    print(f"Total value of count is {count} so that it's a prime number")
else:
    print(f"Total value of count is {count} so that it's a composite number")


num = int(input("Enter any number : "))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print("Number is prime")
else:
    print("Number is composite")


# # GCD
#     if b == 0:
#         return a
#     else:
#         return gcd_rec(b, a % b)
# LCM
#  return (a * b) // gcd_rec(a, b)

print('\n')  # GCD/LCM with Recursion
# this is Euclid's algorithm
def gcd_rec(a, b):
    if b == 0:
        return a  # this is the base case that is going to terminate the recursive function calls because without a
        # base case recursive function calls would call themselves forever and ever. And would never stop
    else:
        return gcd_rec(b, a % b)  # we are switching these two variables a and b because we don't know which number is
        # the larger and do not forget to write gcd_rec() with return
print(gcd_rec(64, 48))
def lcm_rec(a, b):
    return (a * b) // gcd_rec(a, b)
print(lcm_rec(64, 48))

"""
64    48
64 = a
48 = b
64 = 48 x p + reminder  (p is how many times it will multiple with number b)
remainder = a % b
a % b = (16 reminder) we will get the reminder when we will use the modulus operator 
"""

print('\npass statement........')
if 5 > 2:
    pass
else:
    print("Else part")
print("Rest of the code")

if 5 < 2:
    pass
else:
    print("Else part")
print("Rest of the code")

# use of pass
n = 4
i = 1
while i<=n:
    pass
    i = i+1
print("Thanking you")

print('\n')
# How do u check if first letter is digit
ch = '4'  # don't forget to write digit in string form
if ch.isdigit():
    print("The given character", ch, "is a digit")
else:
    print("The given character ", ch, "is not a digit")

# Python Program to check character is Digit or not
txt = "50800"
x = txt.isdigit()
print(x)

print('\nregular expression.........')
import re
text = "Banksia brownii, commonly known as feather-leaved banksia or Brown's banksia, is a species of shrub that grows in the southwest of Western Australia. A banksia with fine feathery leaves and large red-brown flower spikes, it usually grows as an upright bush around two metres (7 ft) high, but can also occur as a small tree or a low spreading shrub. First collected in 1829, it is placed in Banksia subgenus Banksia, section Oncostylis, series Spicigerae. It is considered critically endangered by the International Union for Conservation of Nature; all major populations are threatened by Phytophthora cinnamomi dieback, a disease to which the species is highly susceptible. "
pattern = "was"
match = re.search(pattern, text)
print(match)
text = "Banksia brownii, commonly known as feather-leaved banksia or Brown's banksia, is a species of shrub that grows in the southwest of Western Australia. A banksia with fine feathery leaves and large red-brown flower spikes, it usually grows as an upright bush around two metres (7 ft) high, but can also occur as a small tree or a low spreading shrub. First collected in 1829, it is placed in Banksia subgenus Banksia, section Oncostylis, series Spicigerae. It is considered critically endangered by the International Union for Conservation of Nature; all major populations are threatened by Phytophthora cinnamomi dieback, a disease to which the species is highly susceptible. "
pattern = "is"
match = re.search(pattern, text)
print(match)

text = "Banksia brownii, commonly known as feather-leaved banksia ganksia Danksia and Ganksia Western Australia."
pattern = r"[A-Z]+anksia"  # r is raw string
match = re.search(pattern, text)
print(match)

print('\n')
# it didn't search Danksia and Ganksia b/c re.search look for first match and stop there so, for that we will use...
match = re.finditer(pattern, text)
for matches in match:
    # print(matches, "-->", matches.span(), "-->", type(matches.span()))
    print(text[matches.span()[0]:matches.span()[1]])

print('\n')
txt = "The rain in Spain"
pattern = "^The.*Spain$"
x = re.search(pattern, txt)
print(x)
if x:
  print("YES! We have a match!")
else:
  print("No! We don't have a match!")


print('\n')  # DOCSTRING
def square(n):
    # print(n) # if we will use this line so docstring will print none b/c docstring comes right after function line.
    """Takes in a number n, returns the square of n"""
    print(n ** 2)
square(5)
print(square.__doc__)  # doc can't be ignored like comment


def doc_find(a):
    """Hey, I am Nayan
and who are you,
Can I know your name
    """
    square = 5 ** 2
    return square
a = 5
print(doc_find(a))
print(doc_find.__doc__)


print("\nException Handling.............")
try:
    a = int(input("Enter any number: "))
    print(a + 3)
except:
    print('Some error occurred')

try:
    a = int(input("Enter any number: "))
    print(a + 3)
except Exception as e:
    print('Some error occurred', e)


print('\n')
# The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occurred")
# Since the try block raises an error, the except block will be executed.

print('\n')
try:
    open('open.txt')  # it shows exception ([Errno 2] No such file or directory: 'open.txt' An exception occurred)
except Exception as e:
    print(e)
    # pass
print('Program is alive')

print('\n')
# Many Exceptions: You can define as many exception blocks as you want,
# e.g. if you want to execute a special block of code for a special kind of error:
# exa: Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print('\n')
try:
    file = open('this.txt', 'r')
except EOFError as e:
    print(e)
except IOError as e:
    print("We can handle this error")
finally:
    print("This will be printed irrespective of the exception occurrence")

print('\n')
# In this example, the try block does not generate any error:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print('\n')
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

print('\n')
try:
    print('I will try this code and will throw exception if there is any problem')
except Exception as e:
    print("I will run only if try block fails")
else:
    print("I will run only if there is no exception")
finally:
    print("This will be printed in every case")

print("\nMap, Filter, and Reduce function.............")
# map () function: syntax: map(function, iterable(s))

fruit = ['Apple', 'Banana', 'Pineapple']
map_object = map(lambda s: s[2] == "n", fruit)
print(list(map_object))

# filter () function: syntax: filter(predicate, iterable(s))

fruit = ['Apple', 'Banana', 'Pineapple']
filter_object = filter(lambda s: s[2] == "n", fruit)
print(list(filter_object))

fruit = ['Apple', 'Banana', 'Pineapple']
map_object = map(lambda s: s[0] == "A", fruit)
print(list(map_object))

fruit = ['Apple', 'Banana', 'Pear']
filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object))

print('\n')
# reduce () function: syntax: reduce(function, iterable(s))

from functools import reduce
list1 = [45, 34, 67, 8, -3, -5]
print(reduce(lambda x, y: x + y, list1, 4))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list1, -6)))


print('\n')  # using iteration
l = [1, 2, 4, 5, 6, 4, 3]
newl = []
for item in l:
    cube = item * item * item
    newl.append(cube)
print(newl)

print('\n')  # using function iteration
def cube(x):
    return x * x * x
l = [1, 2, 4, 5, 6, 4, 3]
newl = []
for item in l:
    newl.append(cube(item))  # this cube means we are calling cube here
print(newl)

print('\n')  # using map()
# function in map() function
def cube(x):
    return x * x * x
l = [1, 2, 4, 5, 6, 4, 3]
newsl = map(cube, l)
""" here cube is taking other function as an argument """
print(list(newsl))

# lambda function in map() function
l = [1, 2, 4, 5, 6, 4, 3]
newsl = map(lambda x: x * x * x, l)
print(list(newsl))


def maxi(a):
    return a > 4
l = [1, 2, 4, 5, 6, 4, 3]
newnewl = filter(maxi, l)
print(list(newnewl))


print("\nDecorator......................")  # decorator modify function
def greet(fx):  # this will take another function
    def modified_fx():  # you can use *args and **kwargs here as well
        print('Good Morning')
        fx()  # you can use *args and **kwargs here as well
        print("Thanks for using this function")
    return modified_fx
@greet  # greet is a decorator and it's decorating hello
def hello():
    print("Hello World")
hello()

def hello():
    print("Hello World")
greet(hello)()


print('\n')
def greet(fx):  # this will take another function
    def modified_fx(*args, **kwargs):
        print('Good Morning')
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return modified_fx
def add(a, b):
    print(a + b)
greet(add)(1, 2)  # add() takes 0 positional arguments but 2 were given

@greet
def add(a, b):
    print(a + b)
add(1, 2)  # add() takes 0 positional arguments but 2 were given

print("\nLEGB Rule......................")
x = "awesome"
def myfunc():
    print("python is " + x)
myfunc()

def myfunc():
    global x
    x = "easy"  # if in any case we want to access local value outside the function so, we can use global keyword
myfunc()
print("python is " + x)

x = "5"
def myfunc():
    global x
    x = "123"
myfunc()
print("Python is " + x)

print('\n')
y = 10  # global scope can be used by everyone, both inside and outside of functions
def outer():
    z = 4  # this is nonlocal scope so, this can be used only by local and nonlocal scope
    def inner():
        x = 4
        print("x: ", x)
        print("z: ", z)  # we can access this nonlocal scope "z" in local scope
        print("y: ", y)  # we can access this global scope "y" in local scope
    inner()
    print("z: ", z)  # we can access this nonlocal scope "z" in nonlocal scope
    print("y: ", y)  # we can access this global scope "y" in nonlocal scope
    # print("x: ", x)  # name x is not defined b/c we can't access local scope in nonlocal scope
outer()
print(y)
# print(z)  # name 'z' is not defined b/c we can't access nonlocal scope outside the function (means global)
# print(x)  # name 'x' is not defined  b/c we can't access local scope outside the function


print('\n')
y = 10  # global variable
def inner():
    x = 4  # local variable
    y = 5  # local variable
    print("x:", x)
    print("inside the function y:", y)
print("y:", y)
inner()

# y = 10
# def inner():
#     x = 4
#     y = y + 1  # it will throw an error because you can only change local variable not global variable
#     print("x:", x)
#     print("inside the function y:", y)
#
# print("y:", y)
# inner()

print('\n')
y = 10  # global variable
def inner():
    x = 4  # local variable
    global y  # global keyword means here now you can change global value into local value
    y = y + 1  # local variable
    print("x:", x)
    print("inside the function y:", y)
print("outside the function y:", y)
print("y:", y)  # it will give 10 b/c this is before calling function
inner()
print("y:", y)  # it will give 11 b/c this is after calling function

print("\nNONLOCAL/ Enclosing (nested function)..........................")  # it is used when we have a nested function.
y = 10
def outer():
    z = 4
    def inner():
        x = 4
        nonlocal z
        z = z + 1
        print("x:", x)
        print("inside the function z:", z)
    print("outside the function z:", z)
    print("z:", z)  # it will give 4 b/c this is before calling function
    inner()
    print("z:", z)  # it will give 5 b/c this is after calling function
outer()

print("\nwhile loop.............")
# Infinite while loop (never use because your system or application can be  crush)
# while True:
#     print('Hello')

# Python program to print first 1 to 10 and 10 to 1 natural numbers
n = 10
i = 1  # initialization
while i <= n:  # condition
    print(i, end=" ")
    i = i + 1  # increment

print('\n')
n = 10
i = 1  # initialization
while i <= n:  # condition
    print(n, end=" ")
    n = n - 1  # increment

print('\n')  # Python Program to Find Sum of First n Natural Numbers
n = 10
count = 0
i = 0
while i <= n:
    count = count + i
    i = i + 1
    print(count)

print('\n')
def sumofN(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum  # use return inside for loop not inside sum
print(sumofN(5))


def sumofN(n):
    return (n*(n+1)/2)
print(sumofN(5))


print('\n')  # Python program to find sum of Even numbers from 1 to N.
n = 10
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i = i + 1

n = 10
i = 2  # if you give i = 1 so, it will print all odd number from 1 to 15
while i <= n:
    print(i)
    i = i + 2

print('\n')  # Python program to the sum of Even numbers from 1 to N.
n = 10
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        # print(i)  # 2, 4, 6, 8, 10
        sum = sum + i
        print(sum)
    i = i + 1

print('\n')  # Python program to count the sum of Even numbers from 1 to N.
n = 10
i = 1
sum = 0
count = 0
while i <= n:
    if i % 2 == 0:
        # print(i)  # 2, 4, 6, 8, 10
        sum = sum + i
        # print(sum)
        count = count + 1
        print(i, '=', sum, '=', count)
    i = i + 1

print('\n')  # Python Program to Find Square of First n Natural Numbers  {1 power 2, 2 power 2, 3 power 2, 4 power 2, 5 power 2}
n = 10
i = 1
while i <= n:
    for i in range(1, n + 1):
        squ = i ** 2
        print(squ)
    i = i + 1

n = 10
i = 1
while i <= n:
    square = i * i
    print(square, end=" , ")
    i = i + 1

print('\n')  # Python Program to Find power of numbers from 1 to n  {1 power 1, 2 power 2, 3 power 3, 4 power 4, 5 power 5}
n = 5
i = 1
while i <= n:
    power = i ** i
    print(power, end=" , ")
    i = i + 1

print('\n')  # Python Program to Find Sum of Square of First n Natural Numbers
n = 10
i = 1
sum = 0
while i <= n:
    squ = i * i
    sum = sum + squ
    print(squ, '=', sum)
    i = i + 1

print('\n')  # Python program to find sum of digits of a given number using for loop and while loop.
n = 280198
sum = 0  # for adding use "0" not "1"
for i in str(n):  # TypeError: 'int' object is not iterable so, we converted this into str
    # print(i)
    sum = sum + int(i)  # here we used int to converted back into integer from string
    print(i, '+', sum)


print('\n')  # Python program to find reverse of a given number.

def inttostr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ""
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result
print(inttostr(12345))


n = 2801082
rev = 0  # for adding use "0" not "1"
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)

print('\n')  # Python program to check whether a given number is palindrome or not.
n = 2801082
rev = 0
palin = n
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if palin == rev:
    print(rev, "is palindrome")
else:
    print(rev, "is not palindrome")


print('\n')  # Python program to check whether a given number is armstrong or not.
# # In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself.
n = 153  # 371
sum = 0
arm = n
while n > 0:
    sum = sum + (n % 10) * (n % 10) * (n % 10)  # for armstrong don't use (*10) with sum/rev
    n = n // 10
print(sum)

if arm == sum:
    print("Given number", sum, "is armstrong")
else:
    print("Given number", sum, "is not armstrong")


print("\nF string & STRING FORMAT..............................")
name = 'Nayan'
role = 'Python Developer'
print("Hello, my name is {} and I'm {}".format(name, role))  # in this type of formatting we can do indexing

year = 2024  # int(input("Enter year: "))
if year % 4 == 0:
    print("{0} is a leap year".format(year))  # like this (string formatting)
else:
    print("{0} is not a leap year".format(year))

age = 25
txt = "My name is Nayan, and I am {}"
print(txt.format(age))
name = "Nayan"
txt = "My name is {} and I am 25"
print(txt.format(name))

print('\n')  # The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.56
myorder = "I want {} pieces of {} for {} dollars"
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {2} dollars for{0} pieces of item{1}"  # you can arrange all objects by index
print(myorder.format(quantity, itemno, price))

name = "Nayan"  # % s is used for string
age = 25  # %d is used for numbers
print("My name is %s " % name)
print('Am %d years old' % age)
print("My name is %s and am %d years old" % (name, age))

print("\nsingle underscore (_)...............")
_ = 3  # here variable name is _ (means we can assign this _ as a variable name)
print(_)

numbers = [1, 2, 3, 4, 5]  # (we can also use _ as a temporary variable name)
for _ in numbers:
    print(_, ":", numbers)
print("\n")
# packing concept in single underscore (all values are packed in variable name called "person")
person = 'john', 45, 'NY', 45000
# unpacking concept in single underscore (all values are unpacked, and we can print any specific item)
name, _, _, income = person
print(name)
print(_)  # only latest value of underscore (_) will print here not old vales
print(income)

print("\nsingle trailing underscore (a_)...............")
def getNames(name, class_):
    # we know that class is a built-in keyword so, we can't use it as a variable name but in any case
    # if we want to use pre-defined name as a variable so, we can use trailing underscore with pre-defined keyword.
    pass
getNames('hello', 'xyz')

print("\nsingle leading underscore (_a)...............")
"""
single leading underscore can't be used from user defined module to from  module import *
 (it will throw an error like not defined)
but if you use directly (import module) so, it will not throw an error
"""
class A:
    def __init__(self):
        self.x = 3
        self._y = 4
obj_ref = A()
print(obj_ref.x)
print(obj_ref._y)

class GeeksforGeeks:
    def __init__(self):
        self.geek = "GeeksforGeeks"
obj = GeeksforGeeks()
print(obj.geek)  # TypeError: 'str' object is not callable so, () will not use with obj.geek

# How to print name using default constructor
class GeeksforGeeks:
    # default constructor
    def __init__(self):
        self.geek = "GeeksforGeeks"
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
# creating object of the class
obj = GeeksforGeeks()
# calling the instance method using the object obj
obj.print_Geek()

print("\ndouble leading underscore (__a)...............")  # Inheritance
class Person:
    def __init__(self):
        self.name = 'ABC'
        self._age = 11  # single leading underscore
        self.__city = 'XY'  # double leading underscore
p = Person()
print(p.name)
print(p._age)
# print(p.__city)  # AttributeError: 'Person' object has no attribute '__city'
# print(dir(p))  # '_Person__city' we will call it mangling (this is python interpreter rewrite name)
print(p._Person__city)  # this way you can access city

class Man(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Raja'
        self._age = 45  # single leading underscore
        self.__city = 'NY'  # double leading underscore
    @property
    def age(self):
        return self._age
m = Man()
print(m.name)
print(m.age)
# print(m.__city)  # AttributeError: 'Person' object has no attribute '__city'
# print(dir(m))  # '_Man__city' we will call it mangling (this is python interpreter rewrite name)
print(m._Man__city)  # this way you can access city

print("\ndouble leading and trailing underscore (__a__)...............")
class Person:
    def __init__(self):
        self.__country__ = 'India'
p = Person()
print(p.__country__)
print(Person().__country__)

print("\nNumber System Integer.......................")
# In python, we can write integer in four ways (decimal, binary, hexadecimal, octal)
# computer work on 0 and 1 in collections so that, it works in binary group form means 8/16/32/64 bits
# that's why, we have 32/64 bits computer and mostly computers today's work on 64 bits

print(10_500)  # use underscore at the place of comma. python ignore underscore

"""
To find whether a number is binary, octal, decimal, hexadecimal use--- "o, x, b"
100 is decimal
0o100 is octal (zero and letter “o” capital/small)  
0x100 is hexadecimal (zero and letter “x” capital/small)  
0b100 is binary (zero and letter “b” capital/small)  
"""
# Binary Number system: from 0 to 1 numbers only
# Octal Number system: from 0 to 7 numbers only
# Decimal Number system: from 0 to 9 numbers only
# Hexadecimal Number system: from 0 to 9 numbers and A to F letters only

print('\n')
# from decimal, binary, hexadecimal, octal to DECIMAL
print(1010)
print(0B10101)
print(0x78BFF)
print(0o101)
# print(0o78)  # error because we don't use "8" in octal

print('\n')
# from DECIMAL to decimal, binary, hexadecimal, octal
print(int(65))
print(bin(65))
print(hex(65))
print(oct(65))

print('\n')
print(int(101))
print(bin(0b101))
print(hex(0x101))
print(oct(0o101))

print("\nNumber System Conversion.......................")
# decimal to binary...
print(bin(33))
print(bin(101))  # here we didn't denoted b/c decimal doesn't have any denotation
# 1100101
# 64 32 16 8  4  2  1
# 1  1  0  0  1  0  1  =  101

# binary to decimal...
print(0b101)
print(int(0b101))  # here we denoted 0b b/c we are converting from binary
print(0b1000001)  # it will convert to decimal b/c we didn't use oct

print('\n')
# Python program to convert octal (101) to binary.........
print(bin(0o101))  # for converting octal use 0o
# Python program to convert binary (1000001) to octal.........
print(oct(0b1000001))  # for converting binary use 0b

# Python program to convert octal (33) to binary.........
print(bin(0o33))  # for converting octal use 0o
# Python program to convert binary (11011) to octal.........
print(oct(0b11011))  # for converting binary use 0b

print('\n')
a = 65
# a = 0o101  # this is octal of 65
print(oct(a))  # 0o101
print(bin(a))  # 0b1000001 # we convert octal to binary
print(int(a))  # 65 # we convert octal to decimal
print(hex(a))  # 0x41 # we convert octal to hexadecimal

print('\n')
# octal to ...
a = 0o101  # this is octal
print(a)  # we convert octal to decimal
print(int(a))  # we convert octal to decimal
print(bin(a))  # we convert octal to binary
print(hex(a))  # we convert octal to hexadecimal
print(bin(0o23))

print('\n')
# binary to ...
a = 0b1001010  # this binary
print(oct(a))  # we convert binary to octal
print(bin(a))  # we convert binary to binary
print(int(a))  # we convert binary to decimal
print(a)
print(hex(a))  # we convert binary to hexadecimal

print('\n')
# hexadecimal to binary
print(0x41)  # it will convert to decimal b/c we didn't use bin
print(bin(0x41))
print(bin(0x2d))

# binary to hexadecimal
print(0b101001)  # it will convert to decimal b/c we didn't use hex
print(hex(0b101001))
print(hex(10110111))

print('\n')
# octal to hexadecimal
print(hex(0o101))


print('\n')  # python program to convert float to binary



print("\nBuilt-in () Function.....................")
print("ascii..............................")
# characters and ordinal/ASCII code
# A-Z    65-90
# a-z    97-122
# 0-9    48-57

print("ord..............................")
# ord()	Convert an integer representing the Unicode of the specified character
# convert ASCII unicode Character('A') to 65
y = 'A'
print(ord('A'))
y = ord("A")
print(type(y), y)

print("chr..............................")
# chr()	Returns a character from the specified Unicode code.
# convert integer 65 to ASCII Character('A')
y = 65
print(chr(y))
y = chr(65)
print(type(y), y)

# ch = input('enter a char:- ')
# print(ch)
# ch = input('enter a char:- ')
# print(ch[3])
# ch = input('enter a char:- ')[2:4]
# print(ch)
x = "Hello"
print(x[4])
# unicode: In Python, the built-in functions chr() and ord() are used to convert between Unicode code points and characters.

print("all..............................")
# Return True if all elements of the iterable are true (or if the iterable is empty).
x = all([])
print(x)
x = all("")
print(x)
x = all("Hey")
print(x)  # string object is iterable
# x = all(1)  # TypeError: 'int' object is not iterable
# print(x)

x = all([False, 0])
print(x)
x = all([False, 1])
print(x)
x = all([10, 1])
print(x)

listSame = [1, 1, 1]
newlist = [all([x == 1 for x in listSame])]
print(newlist)

listSame = [1, 1, 1]
print(all([x == 1 for x in listSame]))

listDiff = [1, 2, 3]
print(all([x == 1 for x in listDiff]))

myresult = [True, True, False, True]
print(all(myresult))
myresult = [True, True, True, True]
print(all(myresult))

num1 = [2, 4, 6, 8, 10]
list = []
for i in num1:
    list.append(i)
print(all(list))

numbers = [1, 3, 5, 7, 9, 10]
all_odd = all([n % 2 for n in numbers])
print(all_odd)

numbers = [1, 3, 5, 7, 9]
all_odd = all([n % 2 for n in numbers])
print(all_odd)

numbers = [1, 3, 5, 7, 9]
all_odd = all([(n % 2 == 0) for n in numbers])
print(all_odd)

def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True
iterable = [2, 3, 4, 5, 6]
print(all(iterable))

def all(iterable):
    for element in iterable:
        if element % 2 == 0:
            return False
        return True
iterable = [2, 3, 4, 5, 6]
print(all(iterable))

num1 = [2, 4, 6, 8, 10]
list = []
for i in num1:
    if i % 2:
        list.append(i)
print(all(list))

num1 = [2, 4, 6, 8, 10]
print(all([i % 2 == 0 for i in num1]))

num1 = [2, 4, 9, 8, 13]
print(any([i % 2 == 0 for i in num1]))

print("any..............................")
num1 = [2, 4, 9, 8, 13]
print(any([i % 2 == 0 for i in num1]))

x = any([])
print(x)

boolean_list = [True, False]
print(any(boolean_list))

print('\n')
# Conditions - check for OR
rain = True
cold = False
if rain or cold:
    print("You need a jacket")
else:
    print("you do not need a jacket")

rain = False
cold = True
if rain or cold:
    print("You need a jacket")
else:
    print("you do not need a jacket")

rain = False  # True
cold = False  # True
if rain or cold:
    print("You need a jacket")
else:
    print("you do not need a jacket")


print('\n')  # MCQ...........
print("hello\example\test.txt")
print("hello\\example\\test.txt")  # python doesn't print slash but if you want to print slash so, use double slash
print("hello\"example\"test.txt")
# print("hello"\example"\test.txt")

print('\n')
num = 1, 000, 000  # num will become tuple
print(num)
X_Y_Z = 1, 000, 000  # X_Y_Z will become tuple
print(X_Y_Z)

# output of this
print(f"python{3 + .2}")

a = [5, 10, 15, 20, 25]
k = 1
i = a[1] + 1
j = a[2] + 1
m = a[k + 1]
print(i, j, m)

AL = [1, 2, 3, 4, 5]
print(AL)
AL[2] = []
print(AL)
del AL[2]
print(AL)


print("\nNamespace............")
# Namespace represents a memory block where names are mapped to objects.
# Identifiers are nothing but name in python program. It can be class-name, function-name, variable-name, module name.

print(dir())  # built-in namespace
num = 10
print(dir())  # now it will include num namespace also

a = 50
def func1():
    a = 10
    def func3():
        b = 100
        print(dir())
    print(dir())
    func3()
  # now it will include fun1, func2 namespace also
def func2():
    a = 20
print(dir())
func1()


class Person:
  name = "John"
  age = 36
  country = "Norway"
print(dir(Person))

fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(dir(fruits))

fruits = {"apple", "orange", "banana", "coconut"}
print(dir(fruits))

capitals = {"USA": "Washigton D.c.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
print(dir(capitals))
# print(help(capitals))

print("\n")  # python program, we want a user to enter any number between 100 and 500.
num = int(input("Enter any number between 100 and 500: "))
while num < 100 or num > 500:
    print("Incorrect number")
    num = int(input("Enter any number between 100 and 500: "))
else:
    print("Number is correct", num)

print('\n')  # get list from users
a = []  # user input list # dynamic list
print("Blank list:", a)
n = int(input("Enter number of elements: "))
for i in range(n):
    a.append(int(input("Enter elements: ")))
print("Filled List: ", end="")
print(a)
for element in a:
    print("loop list: ", element)

print('\n')
print('Enter the first number:- ')
firstNumber = int(input())
print('Enter the second number:- ')
secondNumber = int(input())
print(firstNumber + secondNumber)

print("Enter the number: ")
n = int(input())
for i in range(n):
    print("Hello India")


print("\nMultiplication......................")
n = 5
while n <= 50:
    print(n, end=" ")
    n = n + 5

print('\n')
for i in range(5, 51, 5):
    print(i, end=" ")

print('\n')
x = 5
for y in range(1, 11):
    print(x, '*', y, '=', x * y)

print('\n')
for i in range(2, 5):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()


print("\nSyntax of every type Questions......................")
# Syntax of the nested-if-else:
"""
if condition_outer:
    if condition_inner:
        statement of inner if
    else:
        statement of inner else:
    statement of outer if
else:
    statement of outer else
statement outside if block
"""

# Python program to print first 1 to 5 natural numbers
print('\n')
n = 5
i = 1  # initialization
while i <= n:  # condition
    print(i)
    i = i + 1  # increment

# for syntax
'''
for condition:
    if(condition):
        break/Continue
Rest of the code
'''

# pass
'''
while condition:
    if(condition):
        pass
    statements    
Rest of the code
'''

# while syntax
'''
while condition:
    if(condition):
        break/Continue
Rest of the code
'''

# nested loop syntax
"""
for element in sequence
   for element in sequence:
       body of inner for loop
   body of outer for loop
other statements
"""

# exception handled in Python. [Try, Except, Else and Finally Block]
'''
try:
  #some-code....!

except:
    # Optional Block
    # Handling of exception (if required)

else:
    # some code....
    # execute if no exception

finally:
    # some code...(always executed)          
'''

# Count Number (this method returns number of occurrence of a specified element in the list)
"""
syntax: list_name.count(specified_element)
"""

# Syntax: del list[start:end]
# Syntax: list.remove(element)



print('\nPascal Triangle')
"""
when i = 4 and j = 0, 1, 2, 3, 4
j == 0 so, j = 1
list[3][0] + list1[3][1]  1 + 3 = 4
list[3][1] + list1[3][2]  3 + 3 = 6
list[3][2] + list1[3][3]  3 + 1 = 4
j == 4 so, j = 1
"""

n = int(input("Enter number of rows: "))
# get the numbers of the pascal triangle (use nested list)
list1 = []
for i in range(n):  # this for loop is for "row"
    temp_list = []  # inner list name is temp_list in each iteration
    for j in range(i+1):  # this for loop is for "column"
        if j == 0 or j == i:  # value
            temp_list.append(1)  # add this value in temporary list
        else:
            temp_list.append(list1[i-1][j-1] + list1[i-1][j])
# i/j will be current row and (i-1)/ (j-1) will be previous row (we want previous row b/c we are adding previous values)
    list1.append(temp_list)
print(list1)
for i in range(n):
    for j in range(i, n):  # (n, i) == (n-i-1)  but with (n-i-1) you will not get from starting
        print(format("", "<2"), end="")  # this format will print pattern properly  # total 2 places
    for j in range(i + 1):
        print(format(list1[i][j], "<3"), end=" ")  # total 4 places
    print()


print('\nPATTERN LOOP.......................')
x = ['a', 'b', 'c']
y = [1, 2, 3]
for i in x:
    for j in y:
        print(f"{i} = {j}")

print('\n')
x = ['a', 'b', 'c']
for i in range(len(x)):
    for j in range(i + 1):
        print(f"{j} = {x[j]}")

x = ['a', 'b', 'c']
for i in range(len(x)):
    for j in range(i + 1):
        print(f"{j} = {x}")

print('\n')  # Python Program to Print an Inverted Star Pattern
# n = 5
# for i in range(n, 0, -1):
#     print((1, n))

n = 5
for i in range(n, 0, -1):
    print((n - i) * " " + i * "*")  # can use this '* ' or this ' *' at the place of 'x'
print('\n')
for i in range(n, 0, -1):
    print((n - i) * "" + i * " * ")

print('\n')  # Right Triangle:
n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print('\n')  # Downward Triangle:
n = 5
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()

print('\n')  # Right Mirror Triangle: Decreasing triangle of space and increasing triangle of star
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

print('\n')  # Downward mirror Triangle: Increasing triangle of space and decreasing triangle of star
n = 5
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
        # print("", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()


print('\n..............')
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")   # it will be printed like square
        # print("*", end="")  # it will be printed like rectangle
        # print(j, end="")    # it will be printed like square and rectangle in numbers form
    print()  # it is a link to rows and outer loop


# Hill Pattern: Decreasing triangle of space and increasing triangle of star and increasing triangle of star
print('\n')
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):  # if uou will do increment of "i" so, you will not get peak
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()


# Reverse Hill/Pyramid:
print('\n')
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n-1):  # if you will do decrement of "n" so, you will get peak
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()


# Diamond pattern
print('\n')
n = 5
for i in range(n-1):  # if you will do decrement of "n" so, you will get peak from both left and right
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):  # if you will de decrement of "i" so, you will get peak
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n-1):  # if you will do decrement of "n" so, you will get peak
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()


# Sandglass:
print('\n')
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n-1):  # if you will do decrement of "n" so, you will get peak
        print("*", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    for j in range(i, n):
        print(" ", end=" ")
    print()
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):  # if uou will do decrement of "i" so, you will get peak
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i, n):
        print(" ", end=" ")
    print()


# Double Hill Pattern: Decreasing triangle of space and increasing triangle of star and increasing triangle of star
print('\n')
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):  # if you will do decrement of "i" so, you will get peak
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i, n-1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print(" ", end=" ")
    for j in range(i):  # if uyu will do decrement of "i" so, you will get peak
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()


# butterfly
print('\n')
n = 5
for i in range(n-1):  # if you will do decrement of "n" so, you will get peak from both right and left
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()


# Right Pascal's triangle
print('\n')
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i, n-1):   # if you will do decrement of "n" so, you will get peak
        print("*", end=" ")
    print()


# Left Pascal's triangle
n = 5
for i in range(n-1):   # if uou will do decrement of "n" so, you will get peak
    for j in range(i, n):
        print(" ", end=" ")  # This is the right triangle
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")  # This is the left triangle
    for j in range(i, n):
        print("*", end=" ")
    print()


print('\n')
n = 5
for i in range(n):
    for j in range(i, n):
        print("", end=" ")  # this way you can also get peak if you remove space from "". This is the right triangle
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("", end=" ")  # this way you can also get peak if you remove space from "". This is the left triangle
    for j in range(i, n):
        print("*", end=" ")
    print()


print('\n')
print('PATTERN LOOP Numbers.......................')
n = 5
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


print('\n')
n = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(n, end=" ")
    print()


print('\n')
n = 1
for i in range(1, 6):
    for j in range(1, i+1):
        print(n, end=" ")
        n = n + 1
    print()
