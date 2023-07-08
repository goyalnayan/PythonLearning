print("\nFile read/ write......................")
"""
"r" - open a file for reading -default mode
"t" - text mode
"b" - binary mode
"w" - open a file for writing
"x" - creates file if not exist
"a" - Add more content to a file -default mode
"+" - read and write
"""

# open function will return file pointer
f = open("nayan.txt", 'r')  # ('r' and 'rt' both are default mode, if you use 'r' and 'rt' or not you will get same o/p)
print(f)
content = f.read()
print(content)
f.close()  # this is important to close any file
# r can be in binary form or text form (so, use 'b' and 't' with 'r')
f = open("nayan.txt", 'rb')  # this is binary a formate
content = f.read()
print(content)
f.close()

print('\n')
f = open("nayan.txt", 'r')
content = f.read(11)
print('1', content)
content = f.read(11)  # every time you will get different output
print('2', content)
f.close()


print('\n')
f = open("nayan.txt", 'r')  # ('r' and 'rt' both are default mode, if you use 'r' and 'rt' or not you will get same o/p)
for line in f:
    print(line, end='')


print('\n\n')
f = open("nayan.txt", 'r')  # ('r' and 'rt' both are default mode, if you use 'r' and 'rt' or not you will get same o/p)
content = f.readline()
print(content)
content = f.readline()
print(content)
content = f.readline()
print(content)
content = f.readline()
print(content)

f = open("nayan.txt", 'r')
content = f.readlines()
print(content)


# f = open('nayan2.txt', 'w')  # when I use 'w' so it will automatically created nayan2
# content = f.read()
# print(content)
# f.close()


print('\n\n')
file = open('nayan.txt', 'a')
file.write('\nHey I am nayan')
print(file)
with open('nayan.txt', 'a') as file:
    file.write(' and you')
file.close()

print('\n')
# Reading CSV files Using csv.reader()
import csv
with open('nayan.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print('\n')
import csv
with open('nayan.txt', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
