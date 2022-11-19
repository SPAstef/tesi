from sympy import randprime
from random import randint

P = randprime(1000, 10000)
x = randint(1, P)
y = pow(x, -1, P)
z = randint(1, P)
k = (x * y - 1) // P

print(f"p = {P}")
print(f"x = {x}")
print(f"y = inv(x) = {y}")
print(f"k = (xy - 1)/P = {k}")
print(f"z = {z}")
print(f"(z^x)^y = {pow(pow(z, x, P), y, P)}")
print(f"z^(k+1) = {pow(z, k+1, P)}")
