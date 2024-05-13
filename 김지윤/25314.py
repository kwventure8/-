N = int(input()) # 4 <= N <= 1000, N:4의 배수
a = 'int'
for i in range(N//4):
    a = 'long ' + a
print(a)
