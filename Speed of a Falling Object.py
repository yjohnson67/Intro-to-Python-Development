import math

print("Welcome to the velocity calculator.  Please entere the following:")
print()
m = int(input("mass(in kg): ")) #5
g = float(input("Gravity (inm/s^2, 9.8 for Earth, 24 for jupiter): ")) #9.8
t = int(input("Time (in seconds): ")) #10
p = float(input("Density of the fluid (inkg/n^3, 1/3 for air, 1000 for water:)") )#1.3
A = float(input("Cross sectional area (in m^2): "))#0.01
C = float(input("Drag constant (0.5 for sphere, 1/1 for cylinder):")) #0.5

#c = (1 / 2) * p * A * Ccls
c = (1 / 2) * p * A * C
print(f"The inner value of c is: {c:.3f}") #0.03

#v(t) + sqrt(mg/c) * (1 - exp((-sqrt (mgc)/m)t))

velocity = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c)/ m) * t) )#67.512

print(f"The velocity after {t} second is {velocity:.3f}  m/s")
