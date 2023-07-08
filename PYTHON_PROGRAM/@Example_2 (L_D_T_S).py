print('\nlist comprehension..........')
# create a list of odd numbers from 0 to 20.
ls = [i for i in range(20) if i % 2 != 0]
print(ls)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls = [i for i in list1 if i % 2 != 0]
print(ls)

# multiple all elements of list1 to list2 one by one
list1 = [2, 3, 4]
list2 = [12, 13, 14]
ls = [(i*j) for i in list1 for j in list2]  # [i * j] should be inside parenthesis brackets
print(ls)

ls = []
for i in list1:
    for j in list2:
        ls.append(i * j)
print(ls)

# to get multiple element in a element use nested list comprehension
list1 = [2, 3]
list2 = [12, 13, 14]
ls = [(i, j) for i in list1 for j in list2]
print(ls)

ls = []
for i in list1:
    for j in list2:
        ls.append([i, j])  # [i, j] should be inside square brackets
print(ls)

print('\ndict comprehension..........')
# create a dict having square of number of 1 to 8
d = {}
for i in range(1, 8):
    d[i] = i * i  # number is key and square is value
print(d)
for i in range(1, 8):
    d[i] = i ** 2
print(d)
d = {i: i * i for i in range(1, 8)}
print(d)

print('\n')
# Combine two lists into a dictionary, where the elements of the first one serve as the keys and the elements of the second one serve as the values
# Use zip() in combination with dict() to combine the values of the two lists into a dictionary.
list1 = [x for x in range(3)]
list2 = ['Mon', 'Tue', 'Wed']
print(dict(zip(list1, list2)))

dict1 = {}
list1 = [x for x in range(3)]
list2 = ['Mon', 'Tue', 'Wed']
for(key, value) in zip(list1, list2):  # use comma in key, value
    dict1[key] = value
print(dict1)


list1 = [x for x in range(3)]
list2 = ['Mon', 'Tue', 'Wed']
dict1 = {key: value for(key, value) in zip(list1, list2)}  # use semicolon in key: value
print(dict1)


print('\n')
# How to initialize empty List, Tuple, Dict or Set
my_list = list()
print(my_list)
my_tuple = tuple()
print(my_tuple)
my_dict = dict()
print(my_dict)
my_set = set()
print(my_set)

print("\nLIST PROGRAMS...................")
a = [1, 2, 3, 4]
b = []
for i in a:
    b.append(i ** 2)
print(b)

# Python Program to Find the Smallest Divisor of an Integer
n = 56
new_list = []
for x in range(1, n + 1):
    if n % x == 0:
        new_list.append(x)
new_list.sort()
print("\nThe smallest divisor is: ", new_list[0])

# Sort a list without using a sort keyword
list1 = [10, 4, 9, 15, 8]
for i in range(0, len(list1)):  # we use len() when we don't know how many elements user are providing.
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
            # list1[i], list1[j] = list1[j], list1[i]
print("\n", list1)

# Find the pair with given number in a list
listn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
for i in range(len(listn)):
    for j in range(i + 1, len(listn)):
        if listn[i] + listn[j] == target:
            print("pair founded: ", (listn[i], listn[j]), "=", (listn[i] + listn[j]))

# sum of negative number in a list
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0
j = len(given_list) - 1  # -1 that would be the index that corresponds to the last element in the list
while given_list[j] < 0:
    total = total + given_list[j]
    j = j - 1
print(total)

given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
new_list = []
for i in given_list:
    if i < 0:
        new_list.append(i)
print("Negative numbers: ", new_list)
sum = new_list
count = 0
for i in sum:
    count = count + i
print(count)

print('\n')  # Python program to print duplicate for a list in a duplicate_list.
list1 = [1, 2, 3, 1, 4, 2, 5, 6]
unique_list = []
duplicate_list = []
for num in list1:
    if num not in unique_list:
        unique_list.append(num)
    elif num not in duplicate_list:
        duplicate_list.append(num)
print(unique_list)
print(duplicate_list)

print("\nChange list....................")
thislist = list(("apple", "banana", "cherry"))  # it is also possible to use list() constructor when creating a new list
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1] = 'orange'
print(thislist)
print(thislist[0])

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon", "Pineapple"]
print(thislist)

print('\nappend and extend..........')  # list extend and append function
a = [1, 2, 3, 4, 5]
a.append({6})
print(a)
a.append([1, 2])
print(a)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8]
a.append([b])
print(a)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8]
print(a + b)  # this will add all elements in the same list
a.extend(b)
print(a)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b", "c"]
list2 = [4, 5, 6]
for x in list2:
    list1.append(x)
print(list1)

print('\n')
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")  # for append don't use index number
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # for insert use index number
print(thislist)

print('\nRemove, Pop, and del........')
# In how many ways, we can remove elements from the list in python (remove, pop, clear, and del functions)
a = [1, 2, 3, 4, 5]
a.remove(1)
# The remove() method removes the first matching element (which is passed as an argument) from the list.
print(a)

a = [1, 2, 3, 4, 5]
a.pop(1)  # this 1 means it will not remove 1, it means remove value from 1st index (that is 2)
# The pop() method removes an element at a given index, and will also return the removed item.
print(a)

a = [1, 2, 3, 4, 5]
a.pop()
print(a)

a = [1, 2, 3, 4, 5]
a.clear()
print(a)

a = [1, 2, 3, 4, 5]
del a[3]  # this 3 means it will not remove 3, it means remove value from 3rd index (that is 4)
print(a)
# del a
# print(a)

# There are several ways to join, or concatenate, two or more lists in Python.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print("\n")
thislist = ["apple", "banana", "papaya"]  # Copy_lost
mylist = thislist.copy()
print(mylist)
mylist = list(thislist)  # here thislist is under function
print(mylist)


print("\nCustomize/Reverse list....................")
# case Insensitive sort; By default the sort() method is case-sensitive,
# resulting in all capital letters being sorted before lower case letters:
thislist = ["Apple", "cherry", "Papaya", "orange", "kiwi"]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  # for ascending
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
thislist.reverse()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


print('\n')  # reverse list without slicing and without Recursion
def reverse(lst):
    return lst[::-1]
print(reverse([1, 2, 3, 4, 5, 6]))
list1 = [1, 2, 3, 4, 5, 6]
list1.reverse()
print(list1)

list1 = [1, 2, 3, 4, 5, 6]
print(list1[:-1])
print(list1[::-1])

print('\n')  # reverse list without slicing and with Recursion
def rever_lst_rec(l1):
    if not l1:
        return []
    else:
        return [l1[-1]] + rever_lst_rec(l1[:-1])
print(rever_lst_rec([1, 2, 3, 4, 5, 6]))

def rever_lst_rec(l1):
    if not l1:
        return []
    else:
        return [l1[-1:]] + rever_lst_rec(l1[:-1])
print(rever_lst_rec([1, 2, 3, 4, 5, 6]))


b = ["banana", "apple", "microsoft"]  # Reverse_list
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
b = ["banana", "apple", "microsoft"]
b[0], b[2] = b[2], b[0]
print(b)


print('\n')
"""
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
"""
# convert the map into list
def myfunc(a):
    return len(a)
x = (map(myfunc, ('apple', 'banana', 'cherry')))  # map() must have at least two arguments.
print(x)
print(list(x))


print('\n')  # get list from user
list1 = []
n = int(input("Number of elements: "))
for num in range(0, n):
    list1.append(input('Elements: '))
print(list1)

# How to read multiple values from single input? -- By split()
x = list(map(int, input("Enter multiple value: ").split()))
print("List of values: ", x)


print('\nRemoving duplicates........')
lis = [1, 2, 3, 1, 1]
lis = list(dict.fromkeys(lis))
print(lis)


# remove all duplicates not single '1'
lis = [1, 2, 3, 1, 1]
unique_lis = []
duplicate_lis = []
for i in lis:
    if i not in unique_lis:
        unique_lis.append(i)
    elif i not in duplicate_lis:
        duplicate_lis.append(i)
print(unique_lis)  # this list means remove all duplicates and give new list
print(duplicate_lis)

dupli_list = [1, 2, 3, 4, 5, 1, 32, 1, 2, 3, 1]
new_list = []
for i in dupli_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

dupli_list = [1, 2, 3, 4, 5, 1, 32, 1, 2, 3, 1]
new_list = []
[new_list.append(i) for i in dupli_list if i not in new_list]
print(new_list)


list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
list2 = list1
list2[1][2] = 4
print('Old List and ID:', list1, id(list1))
print('New List and ID:', list2, id(list2))


print("\nDICTIONARIES..............................")
# dictionary syntax
"""
my_dictionary = {
        <key>: <value>,
        <key>: <value>,
         .
         .
        <key>: <value>
}
"""

dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
print(list(dict1.fromkeys("USA")))
print(dict1.fromkeys("USA"))
print(list(dict1.fromkeys(dict1)))
print(dict1.fromkeys(dict1))

lis = [1, 2, 3, 1, 1]
print(list(dict.fromkeys(lis)))  # Removing duplicates in list form
lis2 = 0
print(dict.fromkeys(lis, lis2))  # Removing duplicates in dictionary form

tup = ('key1', 'key2', 'key3')
print(list(dict.fromkeys(tup)))
tup = ('key1', 'key2', 'key3')
print(dict.fromkeys(tup))


print('\n')
dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
dict1.copy()  # don't need to use "x"
print(dict1)
dict1.update({'Russia': 'Moscow'})
print(dict1)

dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
dict2 = {"Russia": "Moscow"}
dict1.update(dict2)
print(dict1)


print('\n')
dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
x = list(dict1.values())[1]
print(x)
print(dict1['India'])
x = dict1.get('India')  # need to use "x"
print(x)
x = dict1.pop('India')
print(x)


print('\n')
dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
x = dict1.popitem()
print(x)

dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
dict1.popitem()
print(dict1)

dict1.clear()
print(dict1)

dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
del dict1["India"]
print(dict1)
# del dict1
# print(dict1)


print('\n')
dict1 = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing"}
x = dict1.items()  # this will give answer in tuple and list form
print(x)
x = dict1.keys()
print(x)
x = dict1.values()
print(x)
x = list(dict1.items())
print(x)
x = list(dict1.keys())
print(x)
x = list(dict1.values())
print(x)


print('\n')
capitals = {"USA": "Washigton D.c.", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}
for key in capitals.keys():
    print(key, end=" ")
print('\n')
for value in capitals.values():
    print(value, end=" ")
print('\n')
for item in capitals.items():
    print(item)
print('\n')
for key, value in capitals.items():
    print(f"{key} : {value}")
print('\n')
for key in capitals:
    print(key, "->", capitals[key])
print('\n')
dict = {'nayan': 1, 'goyal': 3, 'sunaina': 2}
for items in sorted(dict.items()):  # Sort dictionary
    print(items)


print('\n')
# Add the key/value pair "color" : "red" to the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car["color"] = "red"
print(car)

print('\nTUPLE............................')
fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(fruits)
print(len(fruits))
print("pineapple" in fruits)
print(fruits.index("banana"))
print(fruits.count('coconut'))

# nested tuple
a = (1, 2, 3)
print(a, a, a)

# we can access tuple using index and slicing tuple like a list in python
tup = (1, 2, 76, "green", True)
# print(tup["green"])  # TypeError: tuple indices must be integers or slices, not str
print(tup[-1])
if 76 in tup:
    print("Yes 76 is present in this tuple")

tup = (1, 2, 3, 4, 5)
print(tup[1])  # Access tuple items
print(tup[-1])  # Negative Indexing
print(tup[2:3])  # Range of Indexes


print('\nConcatenate Tuple..............')
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
print(f"{a} , {b}")

a = (1, 2, 3)
b = (4, 5, 6)
# Ways to concatenate tuples
x = list(a)
y = list(b)
x.extend(y)  # use extend not append
print(x)  # in list form
print(tuple(x))  # in tuple form

# however, we can concatenate two tuples without converting them to list.
countries = ("Spain", "Italy", "India", "England", "Germany")
countries2 = ("Russia",)
temp = countries + countries2
print(temp)

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")  # don't append in new variable (make changes like this)
print(tuple(temp))

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.pop(0)
print(tuple(temp))

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp[2] = "Finland"
print(tuple(temp))


print('\nSET.................')
s = {}
print(type(s))  # this is the type of dict b/c empty set created in dict
s = set()
print(type(s))  # this is the type of set b/c here we used set() function
s = ()
print(type(s))  # this is the tuple b/c of empty square brackets

print('\n')
set1 = {1, 2, 4, 5}  # python set integer is ordered
set2 = {False, True, False}  # python set boolean is ordered
set3 = {1.1, 2.34, 4.4, 5.0}  # python set boolean is ordered
set4 = {'1', '2', '4', '5'}  # python set string is set unordered
print(set1)
print(set2)
print(set3)
print(set4)

print('\n')
set1 = {1, 2, 4, 5}
print(set1)  # no change order at runtime b/c of integer
print(3 in set1)
set1 = {1, 2, 4, 1, 5, 1}
print(set1)  # don't allow duplicates so, it removes


fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)  # change order at runtime b/c of string
print("pineapple" in fruits)
# print(fruits[0])  # 'set' object is not subscriptable
fruits = {"apple", "orange", "banana", "coconut", "coconut"}
print(fruits)  # don't allow duplicates so, it removes


print('\n')
set1 = {1, 2, 4, 5}
set1.copy()
print(set1)
set1 = {1, 2, 4, 5}
set2 = {3, 6}
print(set1, set2)
set1 = {1, 2, 4, 5}
set1.add(3)  # don't use curly brackets in add method
print(set1)
set1 = {1, 2, 4, 5}
set1.update({3})  # use curly brackets in update method
print(set1)
set1 = {1, 2, 4, 5}
set3 = set1.union({3})
print(set3)


print('\n')
set1 = {1, 2, 4, 5}
set1.pop()
print(set1)
set1 = {1, 2, 4, 5}
set1.remove(4)  # this 4 means value 4 not it means index value 5
# (if you want to remove any value so remove it with name/value not from index)
print(set1)
set1 = {1, 2, 4, 5}
set1.discard(4)
print(set1)
set1 = {1, 2, 4, 5}
set1.clear()
print(set1)
set1 = {1, 2, 4, 5}
# del set1[2]  # 'set' object doesn't support item deletion
# print(set1)
# del set1
# print(set1)


# check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")


print('\nSET Methods............................')
# The intersection() method returns a new set whereas intersection_update() method adds item into the existing set from another set.
s1 = {"Tokyo", "Delhi", "Morena"}
s2 = {"Morena", "Mumbai"}
s3 = s1.intersection(s2)
print(s3)
s1.intersection_update(s2)
print(s1)

# symmetric_difference means print the values that are not in common (union "minus" intersection)
print('\n')
s1 = {"Tokyo", "Delhi", "Morena"}
s2 = {"Morena", "Mumbai"}
s3 = s1.symmetric_difference(s2)
print(s3)  # only "morena" is common so, it will not print "morena"
s1.symmetric_difference_update(s2)
print(s1)

# difference() and difference_update() methods print only items that are only present in the original set and not in both sets.
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
print('\n')
s1 = {"Tokyo", "Delhi", "Morena"}
s2 = {"Morena", "Mumbai"}
s3 = s1.difference(s2)
print(s3)
s1.difference_update(s2)
print(s1)

# disjoint sets means two sets are said to be disjoint sets if they have no elements in common
# isdisjoint() (means no intersection) this method check if items of given set are present in another set.
# This method returns False if items are present, else it returns True.
print('\n')
s1 = {"Tokyo", "Delhi", "Morena"}
s2 = {"Morena", "Mumbai"}
print(s1.isdisjoint(s2))

# isuperset() this method checks if all the items of a particular set are present in the original set.
# This method returns True if items are present, else it returns False.
print('\n')
s1 = {"Tokyo", "Delhi", "Morena"}
s2 = {"Morena", "Mumbai"}
print(s1.issuperset(s2))  # False b/c both elements of s2 are not presented in s1
s1 = {"Tokyo", "Delhi", "Morena"}
s3 = {"Morena", "Delhi"}
print(s1.issuperset(s3))  # True b/c both elements of s3 are presented in s1
print(s3.issubset(s1))  # this is opposite from issuperset

# subset() this method check if all item of the original set are also presented in particular set
s1 = {"Tokyo", "Delhi", "Morena"}
s2 = {"Tokyo", "Delhi", "Morena"}
print(s1.issubset(s2))
