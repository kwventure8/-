#2745
line = input().split()
N = line[0] # B진수 숫자 문자열
B = int(line[1]) 
result = 0
sol = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #리스트or문자열
for i,char in enumerate(N[::-1]):
    result += B**i*sol.index(char)
print(result)

result=0
k= len(N)-1
for char in N:
    result+= B**k*sol.index(char)
    k-=1
print(result)
    
