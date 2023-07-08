print('\n')  # Hello, world.
input_string = input()
# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
print(input_string)


print('\n')  # Data Types
"""
Sample Input
12
4.0
is the best place to learn and practice coding!
"""

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2 = int(input())
d2 = float(input())
s2 = str(input())
# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
print(i + i2)
# Print the sum of the double variables on a new line.
print(d + d2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + s2)


print('\n')  # operators
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total_cost = meal_cost + tip + tax
    print(round(total_cost))
if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)


print('\n')  # Intro to Conditional Statements
if __name__ == '__main__':
    N = int(input().strip())
    if N%2 != 0:
        print('Weird')

    elif N>=2 and N<=5:
        if N % 2 == 0:
            print('Not Weird')

    elif N>=6 and N<=20:
        if N % 2 == 0:
            print('Weird')

    elif N>=20 and N % 2 == 0:
        print('Not Weird')

    else:
        print('Not Weird')


print('\n')  # Class vs. Instance


class Person:
    def __init__(self, initialAge):
        if initialAge > 0:
            self.age = initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age = self.age + 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()

    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


print('\n')  # Loops
if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, 11):
        result = n * i
        print(str(n), "x", str(i), "=", str(result))


print('\n')



print('\n')
arr = [1, 3, 5, 7, 9]  # using sort function if numbers are not arranged
a1 = arr[0:4]
print(sum(a1))
a2 = arr[1:5]
print(sum(a2))


print('\n')  # min max sum
def miniMaxSum(arr):
    a = 2 + 3 + 4 + 5
    b = 1 + 3 + 4 + 5
    c = 1 + 2 + 4 + 5
    d = 1 + 2 + 3 + 5
    e = 1 + 2 + 3 + 4
    p = min(a, b, c, d, e)
    q = max(a, b, c, d, e)
    r = (f"{p} {q}")
    return r
print(miniMaxSum([1, 2, 3, 4, 5]))
