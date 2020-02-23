# this program was written by Jordan on 2/23/2020
# this program prints a factorial estimate of an input number and the exact factorial
# problem 6

import math
number = int(input("Enter a number: "))
factorial = 1
for i in range (1,int(number)+1):
    factorial = factorial * i
print("Factorail is",factorial)

factorial_python = math.factorial(number)
print("python formulated factorial = ",factorial_python)
