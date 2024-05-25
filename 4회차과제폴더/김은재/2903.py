#2903
N = int(input()) #시행횟수입력
val = 2 #초기 줄당 점의 갯수
row = 2 #초기 줄의 갯수
for i in range(N): #각 반복에서, 줄과 점은 (2배-1)개가 된다.
    row = row*2-1
    val = val*2-1
P = row * val #점의 갯수
print(P)
