#2563
T = int(input()) #색종이의 수 입력

white = [[0]*100 for i in range(100)] # 100x100 배경

for i in range(T): #검은 색종이를 붙이는 과정
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    x2 = x+10
    y2 = y+10
    for j in range(x,x2):
        for k in range(y,y2):
            white[j][k] += 1 #검은 색 일 경우 +1


S = 0 #면적
for row in white:
    for val in row:
        if val != 0: #0이아닌 값 세기
            S += 1

print(S)
