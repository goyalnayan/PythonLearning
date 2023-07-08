print("\n*args and **kwargs......................")
""" *args take values as tuple and **kwargs take values as dictionary """

def function_name_print(a, b, c, d):
    print(a, b, c, d)
function_name_print("Harry", "Rohan", "Skillf", "Hammad")

print('\n')
def funargs(*args):
    print(type(args))  # whether you provide list or tuple it's type will convert into tuple
    print(args[0])
    print(har)
    for items in args:
        print(items)
har = ["Harry", "Rohan", "Skillf", "Hammad", "The programmer"]
funargs(*har)

print('\n')
def funargs(normal_args, *args):  # at the place of args you can also write argsnayan as well
    # don't use normal_args after *args b/c it will give an error
    print(normal_args)
    for items in args:  # here also use argsnayan
        print(items)
normal_args = 'This is the normal argument and the students are: '
har = ["Harry", "Rohan", "Skillf", "Hammad", "The programmer"]
funargs(normal_args, *har)

print('\n')
def funargs(normal_args, *args, **kwargs):  # at the place of kwargs you can also write kwargsnayan as well
    print(normal_args)
    for items in args:
        print(items)
    print("Now I would like to introduce some of our heroes")
    for key, value in kwargs.items():  # here also use kwargsnayan
        print(key, value)
normal_args = 'This is the normal argument and the students are: '
har = ["Harry", "Rohan", "Skillf", "Hammad", "The programmer"]
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor", "Programmer": "coordinator"}
funargs(normal_args, *har,
        **kw)  # even if you call only normal_arg not args and kwargs so, it will not give an error b/c it is optional

print('\n')
def find_student_name(*args):
    for names in args:
        if names == student_list1:
            print(args)
        else:
            print('incorrect')
student_list1 = ['nayan', 'goyal', 'neo', 'piyush', 'palak']
find_student_name(student_list1)

def find_student_name(*args):
    for names in args:
        if names == student_list1:
            return True
        else:
            return False
student_list1 = ['nayan', 'goyal', 'neo', 'piyush', 'palak']
print(find_student_name(student_list1))

print("\nNested function......................")
# nested function syntax
"""
def outer():
    def inner():
        pass
"""

def disp():
    def show():
        print("Show Function")

    print("Disp Function")
    show()
disp()

def disp():
    def show():
        return "Show Function"
    result = show() + " Disp Function"
    return result
a = disp()
print(a)

print("\nPassing a Function as Parameter......................")
def disp():
    print("Disp function")
def show():
    return "Show function"
disp()
print(show())


def disp(sh):  # I want to get show() as a parameter as sh
    print("Disp function" + sh())  # here sh() means we are calling show function
def show():  # I want to pass this function in disp()
    return " Show function"
disp(show)  # show is my fun name of show()
# this show will pass to sh


print('\n')
def function1():
    print("hi i am function1")
def function2(func):  # FUNCTION as a parameter
    print("hi i am function2 now i will call function1")
    func()
function2(function1)


def function1(func):  # FUNCTION as a parameter
    print("hi i am function1 now i will call function2")
    func()
def function2():
    print("hi i am function2")
function1(function2)

print("\nDecorator......................")
# decorator function syntax
"""
@decorator_function
def my_function():
    pass
"""


def decorator_func(func):
    def wrapper_func():
        print("wrapper_func worked")
        func()
        print("decorator_func worked")
    return wrapper_func
def show():
    print("show worked")
decorator_func(show)()

@decorator_func
def show():
    print("show worked")
show()


print('\n')
def greet(fx):  # greet will take another function as an argument  (fx() is another function as an argument)
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


print("\nLAMBDA FUNCTION..............................")
sq = lambda x, y: x ** y
print(sq(10, 2))

minus = lambda x, y: x - y
print(minus(9, 4))

# how to use lambda in function
def myfunc(n):
    return lambda x: x ** n
mydoubler = myfunc(2)  # this value is for n
mytripler = myfunc(3)
print(mydoubler(5))  # this value is for x
print(mytripler(2))


print('\n')  # Iterator
a = [1, 2, 3, 4]
i = iter(a)
# print(i.__next__())
print(next(i))
print(next(i))
print(next(i))
print(next(i))

list1 = [1, 2, 3, 4, 5, 6]
z = (x ** 3 for x in list1)
print(next(z))
print(next(z))
print(next(z))
print(next(z))

# generator
def sum(a, b):
    s = a + b
    yield s
g = sum(12, 3)
# print(g.__next__())
print(next(g))


print('\n')  # fibonacci series without Recursion
n = 10
x = 0
y = 1
z = 0
for i in range(0, n+1):
    print(z, end=" ")
    x = y
    y = z
    z = x + y

print('\n')  # fibonacci series with Recursion
def fibo(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(4))


def fibo_rec(n):
    if n < 0:
        # print("Incorrect Input")
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fibo_rec(n - 1)) + (fibo_rec(n - 2))
n = 4
print(fibo_rec(n))
for i in range(1, n + 1):
    print(fibo_rec(i), end=" ")

print('\n')  # factorial without Recursion
n = 7
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    i = i - 1
    print(fact, end=" ")

print('\n')  # factorial with Recursion
def fact_rec(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fact_rec(n - 1)
n = 7
print(fact_rec(n))
# Note: factorial (1) is a base case for which we already know the value of factorial.
# The base case is defined in the body of function with this code.
# if num ==1: return 1
