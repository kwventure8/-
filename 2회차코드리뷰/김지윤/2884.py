h, m = input().split()
H = int(h)
M = int(m)

a = (H*60+M-45)//60
if a < 0:
  a = a+24
else:
  a

b = (H*60+M-45)%60
print(a, b)
