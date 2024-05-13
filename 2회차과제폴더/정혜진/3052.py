#3052
li = []

for i in range(10):
  A = int(input())
  if A %42 not in li:
    li.append(A%42)

print(len(li))
