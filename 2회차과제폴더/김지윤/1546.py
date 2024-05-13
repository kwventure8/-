import random

a = int(input())
N = random.sample(range(1, 100), a)
print(N)
M = max(N)

array=[]

for i in N:
  result = float((i/M)*100)
  #print(result)
  array.append(result)

z = sum(array)
print(z/a)
