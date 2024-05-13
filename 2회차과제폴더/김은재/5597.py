#5597
s = []    
for i in range(28):
    s.append(int(input()))
l = []
for j in range(1,31):
     if j not in s:
        l.append(j)
        
print(min(l))
print(max(l))    
    
