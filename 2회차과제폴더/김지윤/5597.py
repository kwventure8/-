import random

a = random.sample(range(1, 31), 28)
a.sort()
print(a)
number = set(range(1, 31)) - set(a)
print(number)
