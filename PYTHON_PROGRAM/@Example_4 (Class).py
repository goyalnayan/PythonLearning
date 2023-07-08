# Use the p1 object to print the value of x:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)


# What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
# class Student(Person):


# class syntax
"""
class ClassName:
    <statement-1>
    .
    .
    <statement-N>
"""

# object syntax (The syntax to create the instance of the class is)
"""
<object-name = <class-name>(<arguments>)>
"""

# class inheritance: Single Inheritance
'''
class derived-class(base-class):
    <class-suite>
'''

# class inheritance: Multi-level Inheritance
'''
class class1:
    <class-suite>
class class2(class1):
    <class-suite>
class class3(class2):
    <class-suite>        
'''

# class inheritance: Multiple Inheritance
'''
class Base1:
    <class-suite>
class Base2:
    <class-suite>
class BaseN:
    <class-suite>     
class Derived(Base1, Base2, .....BaseN):
    <class-suite>       
'''


print('\n')
# Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class.
# Create a function to display all attributes and their values in the Student class.
class Student:
    def __init__(self, n, i):
        self.name = n
        self.id = i

    def info(self):
        print(self.name, self.id)
x = Student("Nayan", 65)
x.info()

print("\nDefine __init__()method...............")
# How do you create a class in python? (To create a class in python, we use the keyword “class”.)
class InterviewbitEmployee:
    def __init__(self, emp_name):
        self.emp_name = emp_name
# To create methods inside the class, we include the methods under the scope of the class as shown below:
    def introduce(self):
        print("Hello I am " + self.emp_name)
# To instantiate or create an object from the class created above:
emp_1 = InterviewbitEmployee("Mr. Employee")
# To access the name attribute, we just call the attribute using the dot operator as shown below:
print(emp_1.emp_name)  # prints Mr. Employee
# The method of the class InterviewbitEmployee can be accessed as shown below:
emp_1.introduce()  # introduce the employee


print('\n')  # A sample class with init method
class Person:
    # init method or constructor
    def __init__(self, name):
        self.name = name
    # sample method
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('\"nayan\"')
print(p.name)
p.say_hi()

p2 = Person('\"rishi\"')
print(p2.name)
p2.say_hi()

print('\n')
class Student:  # class definition
    def __init__(self, fname, lname, age, section):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.section = section
stu1 = Student("Sara", "Ansh", 22, "A2")  # creating a new object
print(stu1.fname, stu1.section)

print('\nCLASSES AND OBJECTS:......................')
class A:  # A is class name identifier without this we can't access function.
    def m1(self):  # here m1 is an identifier without of this, you can't access output.
        print("Nayan")
        print("Neo")
        print("Nain")
r = A()
r.m1()  # Calculate the average of list of numbers


print('\n')
class my_Obj:
    name = 'john'
y = my_Obj()
print(y.name)


print('\n')
class Person:
    name = "Harry"
    occupation = "Developer"
    networth = 10
x = Person()
print(x.name, x.occupation)

x.name = 'Nayan'
x.occupation = 'Astronomer'
print(x.name, x.occupation)


print('\n')
class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
x = Person()  # This is a new Person
y = Person()
z = Person()

x.info()
y.info()
z.info()

print(x.name)
print(x.occupation)

x.name = "Nayan"
x.occupation = "Astronomer"

y.name = "Ushif"
y.occupation = "Astro"

x.info()
y.info()
z.info()  # default value will come if we don't give new name or occupation....


print('\n')
class Employee:
    id = 10
    name = "John"
    occupation = 'wander'
    def display(self):
        print("ID: %d \nName: %s \nOccu: %s" % (self.id, self.name, self.occupation))
        # Creating emp instance of Employee class
emp = Employee()
# del emp.id  # Deleting the property of object
# del emp  # Deleting the object itself
emp.display()


print('\n')
class Robot:
    name = 'Nayan'
    def introduce_self(self):
        print(f"My name is {self.name}, I am {self.doing} with you.")
r1 = Robot()
r1.doing = 'Talking'
r1.introduce_self()


print('\n')
class Robot:
    def introduce_self(self):
        print("My name is " + self.name, "and I am", self.weight)  # self will refer to r1
        print(f"My name is {self.name}, and I am {self.weight}")  # self will refer to r1
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 40

r1.introduce_self()  # self will refer to r1
r2.introduce_self()  # self will refer to r1


print("\nCONSTRUCTORS...........")  # A constructor is a special method in a class

class Robot:
    def __init__(self, name, work):
        self.name = name
        self.work = work
    def introduce_self(self):
        print(f"I am a robot {self.name} and love to {self.work} with humans.")
r1 = Robot('Nayan', 'Talk')
r1.introduce_self()
r1.name = 'GOYAL'
r1.introduce_self()


class Robot:
    def __init__(self, name, doing):
        self.name = name
        self.doing = doing
    def introduce_self(self):
        print(f"My name is {self.name}, I am {self.doing} with you.")
r1 = Robot('Nayan', 'Talking')
r1.introduce_self()


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print("My name is " + self.name)  # self will refer to r1
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
r1.introduce_self()
r2.introduce_self()


print('\n')
class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False
    def introduce_self(self):
        print("My name is " + self.name, "and this is", self.is_sitting)
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)
p1.introduce_self()
p2.introduce_self()

# p1 owns r2 and p2 owns r1
p1.robot_owned = r2
p2.robot_owned = r1
p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self()


print('\n')
class Person:
    def __init__(self):  # initializations
        print('Hey I am a person')
a = Person()
b = Person()

print('\n')
class Person:
    def __init__(self, n, o, s):
        print('Hey I am a person')
        self.name = n  # attribute
        self.occ = o  # attribute
        self.speak = s
    def info(self):
        print(f"{self.name} is a {self.occ}")
        print(self.speak)
c = Person("Harry", "Developer", True)
d = Person("Divya", "HR", False)
c.info()
d.info()


print('\n')  # More than One Constructor in Single class
""" In the below code, the object st called the second constructor whereas both have the same configuration. The first method is not 
accessible by the st object. Internally, the object of the class will always call the last constructor if the class has multiple constructors. """
class Student:
    def __init__(self):
        print("The First Constructor")
    def __init__(self):
        print("The second Constructor")
st = Student()


print('\n')  # How to print name using default constructor
class GeeksforGeeks:
    # default constructor
    def __init__(self):
        self.geek = "GeeksforGeeks"
    # a method for printing data members
    def print_geek(self):
        print(self.geek)
# creating object of the class
obj = GeeksforGeeks()
# calling the instance method using the object obj
obj.print_geek()


print('\n')  # How to add two number using parameterized constructor
class Addition:
    # parameterized constructor
    def __init__(self, f, s):
        self.f = f
        self.s = s
    def display(self):
        # print("First number = " + str(self.first))  # can only concatenate str (not "int") to str
        print(f"First number is:  {self.f}")
        # print("Second number = " + str(self.second))
        print(f"First number is:  {self.s}")
        # print("Addition of two numbers = " + str(self.answer))
        print(f"Addition of two numbers are: {self.answer}")
    def calculate(self):
        self.answer = self.f + self.s
obj1 = Addition(10, 20)
obj1.calculate()
obj1.display()


print('\n')  # Counting the number of objects of a class using constructor
class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1
s1 = Student()
s2 = Student()
s3 = Student()
print("The number of students are: ", Student.count)

print("\nInheritance...........")
# Single Inheritance: Child class derives members of one parent class.
class Parentclass:
    def par_func(self):
        print("I am parent class function")

class Childclass(Parentclass):
    def child_func(self):
        print("I am child class function")

obj1 = Childclass()
obj1.par_func()
obj1.child_func()


# Multi-level Inheritance:
print('\n')
class Animal:
    def speak(self):
        print("Animal Speaking")
# The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
# The child class Dogchild inherits another child class Dog
class Dogchild(Dog):
    def eat(self):
        print("Eating bread...")
d = Dogchild()
d.bark()
d.speak()
d.eat()


print('\n')  # Create a child class Bus that will inherit all the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, time):
        # def run(self, name, max_speed, time):  # this line will give an error so, don't use this
        self.name = name
        self.max_speed = max_speed
        self.time = time
class Bus(Vehicle):
    pass
School_bus = Bus("Volvo", 120, 50)
print(f"My School Bus name is {School_bus.name} and it's speed was {School_bus.max_speed} km in {School_bus.time} mins.")
class Bus_people(Bus):
    def driver(self):
        print(f"My School Bus name is {self.name} and it's speed was {self.max_speed} km in {self.time} mins.")
School_bus = Bus_people("Volvo", 120, 50)
School_bus.driver()

print('\n')  # Multiple Inheritance:
class Calculation1:
    def summation(self, a, b):
        return a + b
class Calculation2:
    def multiplication(self, a, b):
        return a * b
class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b
d = Derived()
print(d.summation(10, 20))
print(d.multiplication(10, 20))
print(d.divide(10, 20))

print("\nbuilt-in class method...........")
# The issubclass(sub,sup) method: The issubclass(sub, sup) method is used to check the relationships between
# the specified classes. It returns true if the first class is the subclass of the second class, and false otherwise.
class Calculation1:
    def summation(self, a, b):
        return a + b
class Calculation2:
    def multiplication(self, a, b):
        return a * b
class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b
d = Derived()
print(issubclass(Derived, Calculation2))  # TypeError: issubclass expected 2 arguments not 3
print(issubclass(Calculation1, Derived))
print(issubclass(Calculation2, Calculation1))


print('\n')
# The isinstance (obj, class) method: The isinstance() method is used to check the relationship between the objects and
# classes. It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.
class Calculation1:
    def summation(self, a, b):
        return a + b
class Calculation2:
    def multiplication(self, a, b):
        return a * b
class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b
x = Derived()
print(isinstance(x, Derived))


print('\n')
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
s = Student('\'NAYAN\'', 2345, 25)
print("Name is %s" % s.name, "with %s" % s.id, "id")

print('\n')
class GeeksforGeeks:
    def __init__(self, geek):
        self.geek = "GeeksforGeeks"
obj = GeeksforGeeks('Geek')
print(getattr(obj, 'geek'))

print("\nbuilt-in class functions...........")
"""
getattr(obj,name,default)	 --> It is used to access the attribute of the object.
setattr(obj, name,value) -->	It is used to set a particular value to the specific attribute of an object.
delattr(obj, name)  -->  It is used to delete a specific attribute.
hasattr(obj, name)  -->  It returns true if the object contains some specific attribute.
"""
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
s = Student('nayan', 2345, 25)
print(getattr(s, 'age'))
setattr(s, 'age', 30)
print(getattr(s, 'age'))
print(hasattr(s, 'age'))
delattr(s, 'id')
# print(s.id)

print("\nbuilt-in class attributes...........")
# Along with the other attributes, a Python class also contains some built-in class attributes
# which provide information about the class.
""" 
__dict__	It provides the dictionary containing the information about the class namespace.
__doc__	It contains a string which has the class documentation
__name__	It is used to access the class name.
__module__	It is used to access the module in which, this class is defined.
__bases__	It contains a tuple including all base classes.
"""

print('\n')
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    def display_details(self):
        print("Name:%s, ID:%d, age:%d" % (self.name, self.id, self.age))
s = Student('nayan', 2345, 25)
s.display_details()
print('\n')
print(s.__dict__)
print(s.__module__)
print(s.__doc__)


print('\n')
# Python Program to Create Dictionary from an Object (Write a Python program to create a class and display the namespace of that class.)
class Capitals:
    def __init__(self, u, i, c):
        self.USA = u
        self.India = i
        self.China = c
capitals = Capitals("Washington D.c.", "New Delhi", "Beijing")
print(capitals.__dict__)

class Dic(object):
    def __init__(self):
        self.USA = 1
        self.India = 2
        self.China = 3
obj = Dic()
print(obj.__dict__)


print('\nclass program........')  # class with name employee (parameter as employee id, name)
class Employee:
    def __init__(self, id, name):  # here I have used __init__ to constructing the class
        self.id = id  # here I used nain at the place of self
        self.name = name
    def info(self):
        print(f"{self.id} and {self.name}")
var = Employee(2108, 'Nayan')
var.info()

print('\nGeometry')
"""
circle 
area = pi * r ** 2
perimeter = 2 * pi * r 

triangle
area = 	1/2 * h * b
perimeter = 2l + b

square 
area = a ** 2
perimeter = 4 * a

Rectangle
area = l * w
perimeter = 2 * (l + w)

Parallelogram
area = h * w
perimeter = 2 * (l + w)
"""

print('\n')  # geometry with Modules and without OOPs
import math
r = 1.1
print(f"The area of circle is:", math.pi * r ** 2)  # also can use 3.14 at pi place
print(f"The perimeter of circle is:", 2 * math.pi * r)

b = 4
h = 2
l = 3
print(f"The area of triangle is:", 0.5 * b * h)
print(f"The perimeter of triangle is:", 2 * l + b)

a = 5
print(f"The area of square is:", a ** 2)
print(f"The perimeter of square is:", 4 * a)

w = 1.5
print(f"The area of rectangle is:", l * w)
print(f"The perimeter of rectangle is:", 2 * (l + w))

print(f"The area of parallelogram is:", h * w)
print(f"The perimeter of parallelogram is:", 2 * (l + w))

print('\n')  # geometry with OOPs (for single)
class Geometry:
    def __init__(self, l, w):
        self.l = l
        self.w = w
class Rectangle(Geometry):
    def rec_area(self):
        self.R_A = self.l * self.w
        return self.R_A

    def rec_peri(self):
        self.R_P = 2 * (self.l + self.w)
        return self.R_P
r1 = Rectangle(3, 2)
print("Area_R: ", r1.rec_area())
print("Perimeter_R: ", r1.rec_peri())

print('\n')  # geometry with OOPs (for all)
import math
class Geometry:
    def __init__(self, r, a, l, b, w, h):
        self.r = r
        self.a = a
        self.l = l
        self.b = b
        self.w = w
        self.h = h
class Rectangle(Geometry):
    def rec_area(self):
        self.R_A = self.l * self.w
        return self.R_A

    def rec_peri(self):
        self.R_P = 2 * (self.l + self.w)
        return self.R_P
class Parallelogram(Rectangle):
    def parall_area(self):
        self.P_A = self.h * self.w
        return self.P_A

    def parall_peri(self):
        self.P_P = 2 * (self.l + self.w)
        return self.P_P
class Triangle(Parallelogram):
    def tri_area(self):
        self.T_A = 0.5 * self.b * self.h
        return self.T_A

    def tri_peri(self):
        self.T_P = 2 * self.l + self.b
        return self.T_P
class Circle(Triangle):
    def cir_area(self):
        self.C_A = math.pi * self.r ** 2
        return self.C_A

    def cir_peri(self):
        self.C_P = 2 * math.pi * r
        return self.C_P
class Square(Circle):
    def sq_area(self):
        self.S_A = self.a ** 2
        return self.S_A

    def sq_peri(self):
        self.S_P = 4 * self.a
        return self.S_P
r = 1.1  # input("Enter the radius: ")
a = 5  # input("Enter the Side: ")
l = 3  # input("Enter the length: ")
b = 4  # input("Enter the breadth: ")
w = 2  # input("Enter the width: ")
h = 1.5  # input("Enter the height: ")
r1 = Square(r, a, l, b, w, h)
print("Rec_area: ", r1.rec_area())
print("Rec_Peri: ", r1.rec_peri())
print("Parall_area: ", r1.parall_area())
print("Parall_Peri: ", r1.parall_peri())
print("Tri_area: ", r1.tri_area())
print("Tri_peri: ", r1.tri_peri())
print("Cir_area: ", r1.cir_area())
print("Cir_peri: ", r1.cir_peri())
print("Sq_area: ", r1.sq_area())
print("Sq_peri: ", r1.sq_peri())

print('\nCalculator')
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
class Addition(Calculator):
    def add(self):
        return self.a + self.b
class Subtraction(Addition):
    def sub(self):
        return self.a - self.b
class Multiplication(Subtraction):
    def mul(self):
        return self.a * self.b
class Division(Multiplication):
    def div(self):
        return self.a / self.b
x = 20
y = 40
v = Division(x, y)
print(f"Addition of {x} + {y} is ", v.add())
print(f"Subtraction of {x} - {y} is ", v.sub())
print(f"Multiplication of {x} * {y} is ", v.mul())
print(f"Division of {x} / {y} is ", v.div())

print(f"Enter your choice between 'a: Addition, s: Subtraction, m: Multiplication, and d: Division = ")
choice = input("Please select the operations between a/s/m/d: ")  # use string for choice b/c a/s/m/d are characters
if choice == 'a':
    print(f" {x} + {y} =", v.add())
elif choice == 's':
    print(f" {x} - {y}=", v.sub())
elif choice == 'm':
    print(f" {x} * {y} =", v.mul())
elif choice == 'd':
    print(f" {x} / {y}=", v.div())
else:
    print("This is an invalid input. Enter only a/s/m/d")

print('\n')  # Python Program to Make a Simple Calculator without class
"""
a. Add  
b. Subtract  
c. Multiply  
d. Divide  
Select operations form a, b, c, d: "c"    
Please enter first number: 11  
Please enter second number: 4  
11 * 4 = 44  
"""

def add(p, q):
    return p + q
def subtract(p, q):
    return p - q
def multiply(p, q):
    return p * q
def divide(p, q):
    return p / q
p = int(input("Please enter first number:- "))
q = int(input("Please enter second number:- "))
print("Please select the operation")
print("a. Adding")
print("b. Subtracting")
print("c. Multiplying")
print("d. Dividing")

choice = input("Please Select operations from a/b/c/d: ")
if choice == 'a':
    print(p, "+", q, "=", add(p, q))
elif choice == 'b':
    print(p, "-", q, "=", subtract(p, q))
elif choice == 'c':
    print(p, "*", q, "=", multiply(p, q))
elif choice == 'd':
    print(p, "/", q, "=", divide(p, q))
else:
    print("This is an invalid input")
