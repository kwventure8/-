#25314
n = int(input())

nol = int(n/4)
if n%4 != 0:
    nol =nol+1
    
long = ""
for i in range(nol):
    long = long +"long "

long = long + "int"
print(long)
