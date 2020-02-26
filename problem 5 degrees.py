# this program was created by Jordan on 2/22/2020
# this program converts radians to degrees
# problem 5
import math
radians = int(input("How many radians?"))
degrees = radians*(180/3.14)
print("non-calculated = ",degrees) # this returns a calculated value.
#The calculations below didn't come out correctly.
#Use:  
#print("Python math.degrees calculated degrees = ", math.degrees(radians))
#The two calculations should return same results.
degrees_python = math.degrees(1)
print("degrees function = ",degrees_python)

