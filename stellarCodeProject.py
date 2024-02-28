import math

x = 0
y = 1
z = 0
yPrime = 0
zPrime = -1/3

n = 3
h = 0.001

while y > 0:
    x = x + h
    y = y + (h * yPrime)
    z = z + (h * zPrime)
    yPrime = z
    zPrime = -(y**n) - (2 * z / x)


print("x: " + str(x) + '\n'
      + "y: " + str(y) + '\n'
      + "z: " + str(z) + '\n'
      + "y\': " + str(yPrime) + '\n'
      + "z\': " + str(zPrime) + '\n')

M = 2 * 2 * 10**30
R = 1.496 * 10**11
mmw = 0.62
G = 6.67 * 10**-11
massH = 1.67 * 10**-24
k = 1.38 * 10**-23

density = -M * x / 4 / 3.14159 / R**3 / z
pressure = G * M**2 / 4 / 3.14159 / (n + 1) / z**2 / R**4
temperature = pressure * mmw * massH / density / k


print("Central density: " + str(density) + " kg/m^3" + '\n'
      + "Central pressure: " + str(pressure) + " Pa  ("
      + str(pressure * 10**-15) + " PPa)" +  '\n'
      + "Central temperature: " + str(temperature) + " K"
      + " (" + str(temperature * 10**-6) + " million K)")

