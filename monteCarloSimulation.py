import random
import math
inside = 0
N = 10 ** 4
for i in range(0, N):
    x=random.random()
    y=random.random()
    if math.sqrt(x * x + y * y) <= 1:
        inside += 1
pi = 4 * inside / N
print('The number of points inside the circle are :', inside)
print ('The value of pi calculated through simulation is ', pi)