# What is a correct syntax to return the first character in a string
name = 'nayan'
print(name[0])

print("\nString Methods..........")
str1 = 'geeks And nayan'
print(str1.casefold())
print(str1.center(25))  # string will come in center and space both side around string
print(str1.count('e'))

print(str1.capitalize())
print(str1.upper())  # all characters are not upper
print(str1.lower())


str1 = 'geeks And nayan'
print(str1.isupper())  # all characters are not upper
print(str1.islower())  # all characters are not lower
str1 = 'NAYAN'
print(str1.isupper())
str1 = 'nayan'
print(str1.islower())

print("\n")
str1 = 'geeks And nayan'
count = 0
for i in str1:
    if count == 'nayan':
        print("Incorrect")
    else:
        count = count + 1
print(count)

str1 = 'geeks And nayan'
print(str1.endswith(' nayan'))
print(str1.endswith(' nayan '))


print('\n')
str1 = 'geeks And nayan'
# Searches the string for a specified value and returns the position of where it was found
print(str1.find('e'))  # this will give index of first string that is specified
print(str1.rfind('n'))  # this will give index of last string that is specified
str1 = "GeeksforGeeks is best for Geeks"
print(str1.index('is'))

str1 = "Nayan goyal is a good girl"
print(str1.startswith('Nayan'))

test_str = "GeeksforGeeks is best for Geeks"  # initializing string
test_sub = "Geeks"  # initializing substring
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)]  # All occurrences of substring in string
print("The start indices of the substrings are : " + str(res))
for i in range(len(test_str)):
    if test_str.startswith(test_sub, i):
        print(i, end=' ')


print('\n')
str1 = "My name is {fname}, I am {age}".format(fname='Nayan', age=25)
print(str1)
str1 = "1234"
print(str1.isdigit())  # Returns True if all characters in the string are digits

str1 = "Nayan Goyal is a Good Girl"
print("#".join(str1))

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

print('\n')
str1 = "     Kiwi     "
x = str1.strip()
print(f"of all fruits {x} is my favorite")  # Returns a both trim version of the string
x = str1.rstrip()
print(f"of all fruits {x} is my favorite")  # Returns a right trim version of the string

print(str1.split())  # Splits the string at the specified separator, and returns a list
print(str1.rsplit())


print('\nRange.......................')
add = []
for i in range(0, 5):
    add.append(i)
print(add)

a = ["apple", "banana", "orange"]
for i in range(3):
    print(i, '-->', a)

k = ['apple', 'mango', 'banana']
for i in range(len(k)):
    print("index: ", i)

k = ['apple', 'mango', 'banana']
for i in k:
    print("index: ", k.index(i))

k = ['apple', 'mango', 'banana']
for i in range(len(k)):
    print("value: ", k[i])

k = ['apple', 'mango', 'banana']
for i in k:
    print("value: ", i)

print('\n')
# Python Program to Print All Numbers in a Range Divisible by a Given Number
n = 12
for x in range(2, 75):
    if x % n == 0:
        print(x)

print('\n')
# Python Program to Find All the Divisors of an Integer
n = 56
for x in range(1, n + 1):  # range will not start from 0 because give a zero division error
    if n % x == 0:
        print(x)

print("\nSTRING PRINT..............................")
str = r"Hello \n How are you?"  # raw string is used to nullify the effect of escape character
print(str)

print('\n')
txt = "Hello\nWorld!"
print(txt)
txt = "Hello\rWorld!"  # well, here in output hello will also come, but it's not printing.....
print(txt)

print('\n')
str = "tutor tjoes"
str = str.replace('t', '~')
print("new string: ", str)

str = "tutor tjoes"
ch = str[0]
str = str.replace(ch, '~')
print("new string: ", str)

str = "tutor tjoes"
ch = str[0]
str = str.replace(ch, "~")
str = ch + str[1:]
print("new string: ", str)

str = "tutor tjoes"
ch = str[0]
str = str.replace(ch, "~~~")
str = ch + str[3:]
print("new string: ", str)

# other parameters of print statement
print("Hey", 6, 7, sep="~")
print("Hey", 6, 7, sep="~", end="009\n")

print("\nString Operators...............")
str1 = "Geeky"
str2 = "Shows"
str3 = str1 + str2
print("Hello" + str3)  # this is concatenated (no space)

str1 = "Geeky"
str2 = "Shows"
str3 = str1, str2  # this will convert into tuple
print("Hello", str3)  # this is comma (space)

print('\n')
a = "Nayan", "Goyal"
print(a)
a = "Nayan"
b = "Goyal"
c = 25
print(a, b, c)

# Repetition Operator is used to repeat the string for several times. It is denoted by *
str = "GeekyShows "
print(str * 5)
print(str[0:5] * 5)

# membership operators
print('y' in 'python')
print('per' in 'operators')
print('Man' in 'manipulation')
print('Pre' not in 'presence')

# Comparison operators
str1 = "A"
str2 = "B"
result = str1 < str2
print(result)

str1 = "program"
str2 = "python"
str3 = "Python"
print(str1 == str)
print(str1 != str2)
print(str2 > str3)
print(str3 < str1)

print("\nCount String...............................")
# Python program to count number of words (of any random string user will input)
from collections import Counter
MyList = ["a", "b", "a", "c", "b", "a"]
a = dict(Counter(MyList))
print(a)

import collections
str = "a"
x = collections.Counter(str)
print(x)

from collections import Counter  # use "s" in collection and "C" should be capital in Counter
str = "GeeksforGeeks"
x = Counter(str)
print(x)

print('\n')
# Write a Python program to calculate the length of a string: (count number of characters in a string)
def str_len(str1):
    count = 0
    for i in range(len(str1)):
        count = count + 1
    return count  # return will come inside "for" not inside "count"
print(str_len('geeksforgeeks'))

str1 = 'geeksforgeeks'
count = 0
for i in range(len(str1)):
    if i == 'Nayan':
        print(i)
    else:
        count = count + 1
print(count)


print('\n')
list1 = [1, 2, 3, 1, 2, 3, 3, 2, 1, 1]
print(list1.count(1))
str = 'nainaneo'
print(str.count('n'))

from collections import Counter
list1 = [1, 2, 3, 1, 2, 3, 3, 2, 1, 1]
print(Counter(list1))
str = 'nainaneo'
print(Counter(str))

print('\nFOR LOOP PROGRAM.......................')
# How to count number of words in a string
str1 = 'nayangoyalneo'
print(str1.count('a'))
print(len(str1))

count = 0
for i in range(0, len(str1)):
    # for i in str1:
    if i == 'Nayan':
        print(i)
    else:
        count = count + 1
print(count)

count = 0
for i in range(0, len(str1)):
    i = i + 1
    count = count + 1
print(count)


print('\n')  # python program to count number of specific character in a string
name = "nayannain"
count = 0
for char in name:
    if char == 'n':
        count = count + 1
print("Total number of n", count)


name = "nayannain"
count = 0
for char in name:
    if char != 'n':
        print(char, end=" ")
    else:
        count = count + 1
print("\nTotal number of n", count)

name = "nayannain"
count = 0
for char in name:
    if char != 'n':
        continue
    else:
        count = count + 1
print("Total number of n:", count)


print('\n')  # Python program to sum of all character in a string
str1 = 'nayangoyalneo'
count = 0
for i in range(0, len(str1)):
    i = i + 1
    count = count + i
    print(i, "=", count)


print('\n')  # Python program to count the sum of all Even numbers from 1 to N.
n = 15
sum = 0
count = 0
for i in range(1, n):
    if i % 2 == 0:
        sum = sum + i
        count = count + 1
        # print(i, count, sum)
        print(f"The 'index' is {count} for {i} = {sum}")
        i = i + 1


print("\nSWAP...............................")
# python program to get a single string from two given strings, separated by a space and swap the first
# two characters of each string.  # Sample String : 'abc', 'xyz'  # Expected Result : 'xyc abz'
a = 'abc'
b = 'xyz'
r = a[:2] + a[2:]
t = b[:2] + b[2:]
print(r + ' ' + t)

# Python program to convert character in swap way......
name = "NAYAN goyal"
print(name.swapcase())

print('\n')
# Python Program to swap the First and the Last Character of a string
# using lists without slicing
string = "NAYAN goyal"
x = list(string)
temp = x[0]
x[0] = x[-1]
x[-1] = temp
print(x)  # print as list
print("".join(x))  # print as string

str = 'Nayan Goyal'
x = str[-1] + str[1:-1] + str[0]  # using slicing
print(x)


name = "NAYAN goyal"
print(name[1:-1])
def swap(str):
    start = str[0]
    end = str[-1]
    swapped_string = end + str[1:-1] + start
    return swapped_string
print(swap("NAYAN goyal"))

print("\nREVERSE...............................")
def reverse(string):
    return string[::-1]
print(reverse("GeeksforGeeks"))

name = "GeeksforGeeks"
for i in range((len(name) - 1), -1, -1):  # start, end, step value (here we know end value)
    print(name[i], end=" ")

str = 'pqrs'
print(list(reversed(str)))


def reverse(str):
    return list(reversed(str))
print(reverse('pqrs'))


def reverse(str):
    reversed_str = "".join(reversed(str))
    return reversed_str
print(reverse("pqrs"))

print('\n')
def reverse(str):
    s = ""
    for i in str:
        # s = s + i  # string will not reverse
        s = i + s
    return s
print(reverse("Geeksforgeeks"))

list1 = [10, 20, 30, 50]
print(list(reversed(list1)))
for num in reversed(list1):
    print(num)

lst = [10, 20, 30, 50]
lst.reverse()
print(lst)

print('\n')
# Write a code to check whether a string is palindrome or not?
a = "nayan"
b = a[::-1]  # here we didn't give end value b/c we don't know how long is string
print(b, end=" is ")
if a == b:
    print("Palindrome String")
else:
    print("Not Palindrome String")

print("\nString Split() Method..............................")
# Split a string into a list where each word is a list item:
a = 'abc' 'xyz'
print(a.split())

a = "Hello, World"
print(a.split(" , "))

print('\n')
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(" ")
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)


def convert(string):
    li = string.split(" ")
    return li
print(convert("america usa"))

print('\n')
# Use a hash character as a separator:
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

# Split the string into a list with max 2 items:
txt = "apple#banana#cherry#orange"
# setting the max-split parameter to 2, will return a list with 3 elements!
x = txt.split("#", 2)
print(x)

print('\n')
# Iterate over words in a sentence using the split() function.
dialogue = "Remember, Red, hope is a good thing, maybe the best of things, and no good thing ever dies"
for word in dialogue.split(" , "):
    print(word)
for word in dialogue.split():
    print(word, end="")

print("\nString join() method...............................")
# Join all items of a list into a string, using an empty string and hash character as separator:
list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))  # joining with empty separator
list1 = "geeks"
print("$".join(list1))  # joining with string "$"

# Join all items in a tuple, using underscore character:
list1 = ('1', '2', '3', '4')
print("_".join(list1))

# Join all items in a set, using dash/hash/dash character:
# Note: Set contains only unique value therefore out of two 4 one 4 is printed.
list1 = {'1', '2', '3', '4', '4'}
print(type(list1))
print("-#-".join(list1))  # set is unordered that's why it's value is changing at runtime.

# Join all items of a dictionary into a string, using the word "TEST" as separator:
# Note: When joining a string with a dictionary, it will join with the keys of a Python dictionary, not with values.
dic = {'Geek': 1, 'For': 2, 'Geeks': 3}
string = '_'.join(dic)  # Joining special character with dictionary
print(string)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
print(mySeparator.join(myDict))

# join() with dictionaries
newDict = {'A': 1, "B": 2}
sep = '->'
print(sep.join(newDict))

# python program to demonstrate the working of the join() method on strings
a = 'HELLO'
b = 'THERE'
z = '-'
z = z.join(a + b)
print(z)

print('\n')
# Find the required output
s = "the sky is blue"
l = s.split()
print(l)
l = l[::-1]
print(l)
l = ' '.join(l)
print(l)

print('\n')
# Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
fname = 'Nayan'
lname = 'Goyal'
rev = fname + ' ' + lname
print(rev)
rev = lname + ' ' + fname
print(rev)
rev = rev[::-1]
print(rev)

print('\n')
def reverse(a, b):
    join_str = "".join((a + " " + b))
    return join_str
print(reverse('abc', 'xyz'))


def reverse(a, b):
    join_str = (a + b).split()
    return join_str
print(reverse('abc', 'xyz'))

def reverse(a, b):
    join_str = (a, b)
    return join_str
print(reverse('abc', 'xyz'))


print("\nString Slicing...............................")
str1 = "nayangoyal, and, shubham."
print(len(str1))
print(str1[0:-7])
print(str1[0:len(str1)-7])
# [0: 25 -7] = [0:18]
print(str1[:-7:])


print('\n')
print(str1[:-7:-1])  # it will get 7 numbers from backwards and then reverse them (-1 means step value)
print(str1[-7:-1])  # it will get 7 numbers from backwards  (-1 means end value so, not will take last string)
k = 7
print(str1[:k][::-1])
print(str1[-4:-2])


print('\n')
str1 = "GeekyShows"
print(str1[3])
print(str1[0:3])
print(str1[0:])
print(str1[::-2])
print(str1[-1:0])  # no result


print('\n')
str1 = "nayangoyal, and, shubham."
print(str1[:])
print(str1[::])  # by default all value will be same

def convert(string):
    list1 = []
    list1[:] = string  # # a copy of the whole array/list (you can even use [:0/1/2/3/] or [::] )
    return list1
print(convert("school"))

# python program to remove first and last char from the string
def swap(str):
    remove_char = str[1:-1]
    return remove_char
print(swap("Tajmahal"))


print("\nString Programs:.....................")
# Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead............
def strings(str1):
    if len(str1) < 2:
        return "empty"  # this string is in quotes not without quotes
    else:
        return str1[0:2] + str1[-2:]
print(strings('nainagoyal'))
print(strings('na'))
print(strings('n'))


# Write a Python program to get a new string from a given string where "And" has been added to the front.
# If the given string already begins with "And" then return the string unchanged.
def string(str1):
    if len(str1) >= 3 and str1[0:3] == 'and':
        return 'unchanged'
    else:
        return 'and' + str1
print(string('andArray'))
print(string('adArray'))
print(string('Numpy'))

# write a python program to create Dictionary from a String............
str1 = "{'A':13, 'B':14, 'C':15}"
dict = eval(str1)  # eval() convert string to dictionary
print(dict)
print(dict['A'])

# Remove punctuations (Except space)
str1 = "/*apples are & found% only @red &and green"
for i in str1:
    if (i >= 'A' and i <= 'z') | (i >= 'a' and i <= 'z') | (i == ' '):
        print(i, end="")

print('\n')
str1 = "/*apples are & found% only @red &and green"
s = ''
for i in str1:
    if (i >= 'A' and i <= 'Z') | (i >= 'a' and i <= 'z') | (i == ' '):
        # if ((i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i == ' ')):
        s = s + i
print(s)

print('\n')
# python program to check whether a string characters are vowel or consonant
# chr = input("Enter any character: ")
chr = 'N'
for c in chr:
    if (
            c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U' or c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        print("Character is Vowel")
    else:
        print("Character is consonant")

chr = 'g'  # input("Enter any character: ")
for c in chr:
    U_Vowel = ['A', 'E', 'I', 'O', 'U']
    L_Vowel = ['a', 'e', 'i', 'o', 'u']
    if c in U_Vowel or c in L_Vowel:  # this is membership operator so don't use '==' sign rather use in operator
        print("Character is Vowel")
    else:
        print("Character is consonant")

print('\n')
# python program to count number of vowel or consonant in a string
# chr = input("Enter any String: ")
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

a = 'naina'
for i in range(0, len(a)):
    print(a[i])  # we used slicing    # a[i] will give string one by one
    i = i + 1

a = 'naina'
for i in range(0, len(a)):
    print(i)  # i will give index
    i = i + 1


def string(ch):
    vowel = 0
    cons = 0
    for i in range(0, len(ch)):
        lower_v = ['a', 'e', 'i', 'o', 'u']
        upper_v = ['A', 'E', 'I', 'O', 'U']
        if (ch[i] in lower_v) or (ch[i] in upper_v):
            vowel = vowel + 1
        else:
            cons = cons + 1
    return vowel, cons
print(string("\nnayangoyalneo"))
vowel, cons = string("nayangoyal")
print("vowel", vowel)
print("consonant", cons)


print('\n')  # Find middle character from a string
string1 = 'nayangoyal'  # input("Enter the string: ")
print("String is ", string1)
middle = int(len(string1) / 2)
# print("The middle character is ", str(middle))  # this will give you answer in string form (also use [] brackets)
print("The middle character is ", middle)  # this will give you answer in int form
print("The middle character is ", string1[middle])  # this will give you answer in string form (also use [] brackets)
# print("The middle character is ", str[middle])  # type 'str' is not subscriptable (so don't use this)


print('\n')  # Python program to count total string words
test_string = input("How many string you want to know so, write them in detail : ")
total = 1
for i in range(len(test_string)):
    if test_string[i] == ' ' or test_string == '\n' or test_string == '\t':
        # if (test_string[i] == '' # (this means we are giving no space so, it means every string word will count as single)
        total = total + 1
print("Total Number of Words in our input strings are:", total)


print("\nSTRING Methods..............................")
# Strings are immutable so, we can't change string but, we can create new string by applying string methods
a = "Nayan_Goyal"
print(a.replace("_", "Astro"))
print(a.replace("a", "*"))

a = "He's name is Dan. Dan is an honest man"
print(a.find("nes"))
print(a.find("man"))
print(a.find("man "))  # it will not give an error (if given value is absent from the string then return -1)

print(a.index("nes"))
print(a.index("man"))
# print(a.index("man "))  # it will give an error (If given value is absent from the string then raise an exception)


""" isalnum() method returns true only if the entire string only consists of A-Z, a-z, 0-9. If any other whitespace, 
characters, or punctuations are present, then it return False."""

a = "GeekyShows2"  # True because of only letters and number
print(a.isalnum())
a = "Geeky Shows"  # False because of whitespace
print(a.isalnum())
a = "Geeky_Shows"  # False because of character (_)
print(a.isalnum())

""" isalpha() method returns true only if the entire string only consists of A-Z, a-z. If any other whitespace, 
characters, numbers(0-9), or punctuations are present, then it return False."""

a = "GeekyShows"  # True because of no space
print(a.isalpha())
a = "GeekyShows2"  # False because of number
print(a.isalpha())
a = "Geeky Shows"  # False because of whitespace
print(a.isalpha())
a = "Geeky_Shows"  # False because of character (_)
print(a.isalpha())

a = "nayan"
print(a.islower())  # all string letter should be small
a = "NAYAN"
print(a.isupper())  # all string letter should be upper
a = "Nayan"
print(a.islower())
print(a.isupper())

print('\n')
a = "We wish you a Merry Christmas"
print(a.isprintable())
a = "We wish you a Merry Christmas\n"
print(a)  # it will not print '\n' but it will only give space
print(a.isprintable())  # false because \n is not printable

a = " "  # using space bar
print(a.isspace())
a = "World Health Organization"  # print true only if every first words has capitalized
print(a.istitle())
a = "World Health organization"  # print false b/c all first words are not capitalized
print(a.istitle())  # it will capitalize every first letter of word
print(a.title())
print(a.startswith("World"))
print(a.swapcase())  # convert upper to lower and lower to upper
