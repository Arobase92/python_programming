from math import sqrt


a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of b: "))
delta = b**2-4*a*c
x_1 = (-b + sqrt(delta))/(2*a)
x_2 = (-b - sqrt(delta))/(2*a)

print(f"The roots are {x_1} and {x_2}")