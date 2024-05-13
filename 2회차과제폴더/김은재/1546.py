#1546
N = int(input())
score = list(map(int,input().split()))
M = max(score)
mean = 0
for i in range(N):
    score[i] = score[i]/M*100
    mean = mean+ score[i]
mean = mean/N
print(mean)


    
