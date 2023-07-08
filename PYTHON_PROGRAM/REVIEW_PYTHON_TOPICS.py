# how to multiply every number in order
def power(num):
    if num<1:
        return 0
    elif num==1:
        print(1)
        return 1
    else:
        prev = power(num//2)
        curr = prev*2
        print(curr)
        return curr
print(power(45))


print('\n')
def mod(a, b):
    if b<=0:
        return -1
    div = a//b
    return a- div*b
print(mod(5, 3))


# dec_num = float(input("Enter decimal number: - "))
# bin_num = 0
# i = 0
# while dec_num != 0:
#     r = dec_num % 2
#     bin_num = bin_num + r * (10 ** i)
#     dec_num = dec_num/2
#     i = i + 1
# print('Binary converted form; bin_num')

"""
# F = (c*1.8) + 32
# C = (f-32) * 5/9
# inches = 0.394*cm
# feet = 0.0328*cm

# reverse
# rev = rev * 10 + n % 10
# Armstrong
# sum = sum + (n % 10) * (n % 10) * (n % 10)

# # GCD
#     if b == 0:
#         return a
#     else:
#         return gcd_rec(b, a % b)
# LCM
#  return (a * b) // gcd_rec(a, b)


# return fibo(n-1) + fibo(n-2)  "if n == 1 return 0"
# return n * fact_rec(n - 1)  "if n == 1 return 1"
"""


print('\n')  # how to swap two number
a = 1
b = 8
# a, b = b, a
temp = a
a = b
b = temp
print(a, b)


print('\n')
"""
Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). 
"""
num = [10, 20, 30, 40]
resultN = map(lambda x:x*x, num)
print(list(resultN))

# num = [10, 20, 30, 40]
# resultN = lambda x:x*x, num
# print(resultN)

print('\n')
# fibonacci
def fibo(n):
    if n < 0:
        print("number is incorrect")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(7))

# factorial
def fact(n):
    if n < 0:
        print("number is incorrect")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * fact(n-1)
print(fact(5))

# prime
n = 6
sum = 0
for i in range(1, n+1):
    if n%i == 0:
        sum = sum + 1
if sum == 2:
    print('prime')
else:
    print('composite')