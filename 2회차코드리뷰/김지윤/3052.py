import random

b = 42
mod = set()
print(" a", " b", " a%b")

for _ in range(10):
    a = random.randint(0, 1000)
    print(a, b, a%b)
    mod.add(a%b)

count = len(mod)
print("")
print(count)
