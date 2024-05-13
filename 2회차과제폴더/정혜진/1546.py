#1546
A = int(input())
B = list(map(int, input().split()))

maxV = max(B)
C = 0

for j in range(A):
  C += (B[j]/maxV*100)

print(C/A)
