import random
import math

n = 10000000
n_in_circle = 0

for i in range(n):
    x = random.random()
    y = random.random()

    if math.sqrt(x**2 + y**2) <= 1:
        n_in_circle += 1

pi = 4 * n_in_circle / n

print(str(pi))
