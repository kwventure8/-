#3052
num = []
for i in range(10):
    num.append(int(input()))

l = []
for j in num:
    l.append(j%42)
l2 = list(dict.fromkeys(l))
print(len(l2))
