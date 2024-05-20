#1316번
N= int(input())
result = 0
for i in range(N):
    str1 = input()
    l = []
    o = []
    for j in range(len(str)):
        b = str1[j]
        if b not in l:
            l.append(b)
        elif str1[j-1] != b:
            o.append(b)
    if len(o) == 0:
        result = result+1
        
print(result)
